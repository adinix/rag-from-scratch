def sort_key(r):
    return (r[2], r[1])


class Service:
    def __init__(self,embedder, pg_vec, chunker, generator, logger, reranker):
        self.embedder = embedder
        self.pg_vec = pg_vec
        self.chunker = chunker
        self.generator = generator
        self.logger = logger
        self.reranker = reranker
        
    def add_doc(self, title, source):
            doc_id = self.pg_vec.add_doc(title, source)
            return doc_id
        
    def ingest(self, doc_id, text):
        chunks = self.chunker.chunk_paragraphs(text)
        embeddings, embedding_usage = self.embedder.embedding_text(chunks)
        self.pg_vec.add_chunks(doc_id, chunks, embeddings)
        
    def embed_quest(self, question, candidate_limit, threshold):
        embedded_quest, usage = self.embedder.embedding_text(question)
        result = self.pg_vec.searching(embedded_quest[0], candidate_limit)
        good = [r for r in result if r[3] < threshold]
        good.sort(key=sort_key)
        return good, usage
    
    def make_str(self, result):
            string_list = []
            for i in range(len(result)):
                string_list.append(f"[{i+1}] {result[i][0]}")
            return "\n\n".join(string_list)
            
    def answer(self, question, limit, threshold, candidate_limit):
        chunks, embedding_usage = self.embed_quest(question, candidate_limit, threshold)
        if chunks:
            candidate_context = self.make_str(chunks)
            ranked_list, ranked_usage = self.reranker.rerank(candidate_context, question)
            selected_chunks = []
            seen = set()
            for label in ranked_list.indexes:
                if len(selected_chunks) == limit:
                    break
                if label < 1 or label > len(chunks):
                    continue
                if label in seen:
                    continue
                seen.add(label)
                selected_chunks.append(chunks[label - 1])
            if not selected_chunks:
                selected_chunks = chunks[:limit]
            selected_context = self.make_str(selected_chunks)
            answer, generation_usage = self.generator.answer(selected_context, question)
            return answer, selected_chunks, embedding_usage, generation_usage, ranked_usage
        return "I don't have anything on that", [],embedding_usage, None, None
