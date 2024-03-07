from typing import Optional
from pydantic import BaseModel, Field


class CodeCorrAnswerSchema(BaseModel):
    assigment_token: str = Field(...)
    answer: str = Field(...)
    result: Optional[object]
    corr_percentage: Optional[float]
    class Config:
        schema_extra = {
            "example": {
                "assigment_token": "",
                "answer": "print('hello world')\nprint('test code correction')",
            }
        }