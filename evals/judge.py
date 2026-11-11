from models import JudgeResult 

class Judge:
    def __init__(self, model, client):
        self.model = model
        self.client = client
        
    
    def judge_model(self, question, answer, chunks):
        response = self.client.responses.parse(
            model = self.model,
            text_format = JudgeResult,
            reasoning = {"effort": "low"},
            input = [
                {"role": "developer", "content": "You check answers from RAG app. You get some documents, a question, and an answer. Say if everything in the answer comes from the documents. Don't use your own knowledge. 'I don't know is only correct when the documents dont't have the answer."},
                {"role": "user", "content": f"documents: {chunks}\n\nQuestion:{question}\n\n Answer: {answer}"}
            ],
        )
        return response.output_parsed
