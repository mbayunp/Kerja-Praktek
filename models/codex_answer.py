from typing import Optional
from pydantic import BaseModel, Field


class CodexAnswerSchema(BaseModel):
    token_assigment: str = Field(...)
    id_bahasa_program: str = Field(...)
    answer: str = Field(...)
    result: Optional[list]
    class Config:
        schema_extra = {
            "example": {
                "token_assigment": "",
                "id_bahasa_program": "",
                "answer": "print('hello world')\nprint('test code correction')",
            }
        }