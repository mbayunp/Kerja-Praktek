from typing import Optional
from pydantic import BaseModel, Field


class CodexAssigmentSchema(BaseModel):
    id_bahasa_program: str = Field(...)
    output_answer: str = Field(...)
    input: Optional[str]
    testcase: int = Field(..., gt=-1, lt=100)
    condition_test: Optional[list]
    class Config:
        schema_extra = {
            "example": {
                "id_bahasa_program":"70",
                "output_answer": "hello world\ntest code correction",
                "input": "hello",
                "testcase":0,
                "condition_test":[
                    {
                        "input":" ",
                        "output":" "
                    }
                ]
            }
        }
