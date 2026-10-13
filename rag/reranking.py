from models import Ranking
class Reranker:
    def __init__(self, model, client):
        self.model = model
        self.client = client
        
    def rerank(self, context, question):
        response = self.client.responses.parse(
            model = self.model,
            reasoning = {"effort" : "low"},
            text_format = Ranking,
            input = [
                {
                    "role": "developer",
                    "content": ( 
                        "Rank the chunks from most useful to least useful for answering the question. "
                        "Return their numbered labels in indexes. "
                        "use every label once, and don't add any other number. "
                        "dont answer the question."
                    ),
                },
                {
                    "role": "user", 
                    "content": f"<documents>\n{context}\n</documents>\n\n<question>\n{question}\n</question>",
                },
            ]  
        )
        return response.output_parsed, response.usage
