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
                {"role": "developer", "content": "You are grading a rag system. you are given a source document, question and answer. Decide if EVERY claim in answer is supported by documents. Ignore outside knowledge. if the answer is 'I dont know', that is fine only when the documents really don't have the answer."},
                {"role": "user", "content": f"documents: {chunks}\n\nQuestion:{question}\n\n Answer: {answer}"}
            ],
        )
        return response.output_parsed
