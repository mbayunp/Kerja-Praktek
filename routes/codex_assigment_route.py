from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from controlers.codex_assigment_controler import (
    add_assigment,
    retrieve_assigments,
    retrieve_assigment,
    delete_assigment,
    retrieve_languages,
)

from models.response import (
    ResponseModel,
    ErrorResponseModel
)

from models.codex_assigment import (
    CodexAssigmentSchema
)

router = APIRouter()

@router.post("/", response_description="Assigment data added into the database")
async def add_assigment_data(assigment: CodexAssigmentSchema = Body(...)):
    assigment = jsonable_encoder(assigment)
    new_assigment = await add_assigment(assigment)
    return ResponseModel(new_assigment, "Assigment added successfully.")

@router.get("/languages", response_description="Program Languages retrieved")
async def get_languages():
    lang = await retrieve_languages()
    if lang:
        return ResponseModel(lang,"Data ID Languages")
    return ErrorResponseModel("An error occurred.", 404, "Judge0 doesn't connected.")

@router.get("/", response_description="Assigment retrieved")
async def get_assigments():
    assigment = await retrieve_assigments()
    if assigment:
        return ResponseModel(assigment, "Assigment data retrieved successfully")
    return ResponseModel(assigment, "Empty list returned")

@router.get("/{token_soal}", response_description="Assigment data retrieved")
async def get_assigment_data(token_soal):
    assigment = await retrieve_assigment(token_soal)
    if assigment:
        return ResponseModel(assigment, "Assigment data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Assigment doesn't exist.")

@router.delete("/{token_soal}", response_description="Assigment data Successfully Deleted")
async def delete_assigment_data(token_soal):
    assigment = await delete_assigment(token_soal)
    if assigment:
        return ResponseModel(assigment, "Assigment data Successfully Deleted")
    return ErrorResponseModel("An error occured.",404,"Assigment doesn't exist.")

