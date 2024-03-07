from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controlers.codex_answer_controler import(
    add_answer,
    retrieve_answers,
    retrieve_answer,
)

from models.response import (
    ResponseModel,
    ErrorResponseModel
)

from models.codex_answer import (
    CodexAnswerSchema,
)

router = APIRouter()

@router.post("/", response_description="Answer data added into the database")
async def add_answer_data(answer: CodexAnswerSchema = Body(...)):
    answer = jsonable_encoder(answer)
    new_answer = await add_answer(answer)
    if new_answer == False:
        return ErrorResponseModel("Token Salah",404,"Token Assigment tidak bisa ditemukan")
    return ResponseModel(new_answer, "Assigment added successfully.")

@router.get("/", response_description="Answer retrieved")
async def get_answers():
    answer = await retrieve_answers()
    if answer:
        return ResponseModel(answer, "Assigment data retrieved successfully")
    return ResponseModel(answer, "Empty list returned")

@router.get("/{token_soal}", response_description="Answer data retrieved by Assigment token")
async def get_answer_data(token_soal):
    answer = await retrieve_answer(token_soal)
    if answer:
        return ResponseModel(answer, "answer data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Answer doesn't exist.")
