from pydantic import BaseModel, Field, field_validator

class QuestionIn(BaseModel):
    question : str = Field(min_length=1, max_length=1000)
    
    @field_validator("question")
    @classmethod
    def strip_question(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("question can not be blank")
        return v

class JudgeResult(BaseModel):
    faithful: bool
    reason: str
    
class Ranking(BaseModel):
    indexes : list[int]
