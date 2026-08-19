class Generator:
    
    def __init__(self, model, client):
        self.model = model
        self.client = client
        
    def answer(self, context, question):
        response = self.client.responses.create(
            model = self.model,
            reasoning = {"effort": "low"},
            input = [
                {"role": "developer", "content": "answer based only on the documents provided, if the answer is not in them, say you dont know. Never use outside knowledge. Cite the source number in brackets, like [1], after each fact you use."},
                {"role": "user", "content": f"Documents: \n{context}\n\n{question}"}
            ],
        )
        return response.output_text
