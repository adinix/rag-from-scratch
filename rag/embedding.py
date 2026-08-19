class Embedding:
    def __init__(self, model, client):
        self.model = model
        self.client = client
    
    def embedding_text(self, texts):
        response = self.client.embeddings.create(
            input=texts,
            model=self.model
        )

        embeddings = []
        for item in response.data:
            embeddings.append(item.embedding)
        return embeddings
