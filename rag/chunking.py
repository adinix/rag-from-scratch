class Chunker:
    def __init__(self, size, overlap_size):
        self.size = size
        self.overlap_size = overlap_size

    def chunk_text(self, text):
        if self.overlap_size >= self.size:
            raise ValueError("overlap must be smaller than size")
        chunks = []
        i = 0
        while i < len(text):
            chunks.append(text[i: i + self.size])
            i += self.size - self.overlap_size
        return chunks

    def chunk_paragraphs(self, text):
        paragraphs = text.split("\n\n")
        chunks = []
        current = ""
        i = 0
        while i < len(paragraphs):
            if len(paragraphs[i]) > self.size:
                if current:
                    chunks.append(current)
                    current = ""
                chunks_list = self.chunk_text(paragraphs[i])
                for p in chunks_list:
                    chunks.append(p)
                i += 1
                continue
            if len(paragraphs[i]) + len(current) <= self.size:
                if current:
                    current += "\n\n" + paragraphs[i]
                else:
                    current += paragraphs[i]
                i += 1
                continue
            chunks.append(current)
            current = ""
            current += paragraphs[i]
            i += 1
        if current:
            chunks.append(current) 
        return chunks
