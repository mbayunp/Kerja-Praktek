from typing import Optional
from pydantic import BaseModel, Field


class CodeCorrAssigmentSchema(BaseModel):
    soal: str = Field(...)
    id_bahasa_program: str = Field(...)
    idx_error: int = Field(..., gt=0, lt=100)
    soal_err: Optional[str]
    output: Optional[str]
    error_check: Optional[dict]
    class Config:
        schema_extra = {
            "example": {
                "soal": "print('hello world')\nprint('test code correction')",
                "id_bahasa_program":"70",
                "idx_error": 3,
            }
        }

