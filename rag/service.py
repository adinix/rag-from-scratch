
def sort_key(r):
    return (r[2], r[1])


class Service:
    def __init__(self,embedder, pg_vec, chunker, generator):
        self.embedder = embedder
        self.pg_vec = pg_vec
        self.chunker = chunker
        self.generator = generator
        
    def add_doc(self, title, source):
            doc_id = self.pg_vec.add_doc(title, source)
            return doc_id
        
    def ingest(self, doc_id, text):
        chunks = self.chunker.chunk_paragraphs(text)
        embeddings = self.embedder.embedding_text(chunks)
        self.pg_vec.add_chunks(doc_id, chunks, embeddings)
        
    def embed_quest(self, question, limit, threshold):
        embedded_quest = self.embedder.embedding_text(question)
        result = self.pg_vec.searching(embedded_quest[0], limit)
        good = [r for r in result if r[3] < threshold]
        good.sort(key=sort_key)
        return good
    
    def make_str(self, result, question):
        if not result:
            return "I dont have anything on that"
        else:
            string_list = []
            for i in range(len(result)):
                string_list.append(f"[{i+1}] {result[i][0]}")
            ai_ans = self.generator.answer("\n\n".join(string_list),question)
            return ai_ans
