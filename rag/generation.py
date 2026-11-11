class Generator:
    
    def __init__(self, model, client):
        self.model = model
        self.client = client
        
    def answer(self, context, question):
        response = self.client.responses.create(
            model = self.model,
            reasoning = {"effort": "low"},
            input = [
                {"role": "developer", "content": "Answer using only the documents. If the answer isn't there, say you don't know. Don't use your own knowledge or add your own conclusions. Keep every condition exactly as the document says it. Cite the source after each fact, like [1]."},
                {"role": "user", "content": f"Documents: \n{context}\n\n{question}"}
            ],
        )
        return response.output_text, response.usage
