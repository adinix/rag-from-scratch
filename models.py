from pydantic import BaseModel

class QuestionIn(BaseModel):
    question : str
