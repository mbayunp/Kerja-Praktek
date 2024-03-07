from bson.objectid import ObjectId
from utils.devops import codexconndb
from repositories.generate_token import mkid
import repositories.exec_code as exec_code



assigment_collection = codexconndb()["dbsoal"]

def assigment_helper(assigment) -> dict:
    return {
        "id": str(assigment["_id"]),
        "token_assigment": assigment["token_assigment"],
        "id_bahasa_program": assigment["id_bahasa_program"],
        "output_answer": assigment["output_answer"],
        "input": assigment["input"],
        "testcase": assigment["testcase"],
        "condition_test": assigment["condition_test"],
    }



# Add a new student into to the database
async def add_assigment(assigment_data: dict) -> dict:
    assigment = await assigment_collection.insert_one(
        {
            "token_assigment":mkid(),
            "id_bahasa_program": assigment_data["id_bahasa_program"],
            "output_answer":assigment_data["output_answer"],
            "input": assigment_data["input"],
            "testcase": assigment_data["testcase"],
            "condition_test": assigment_data["condition_test"],
        }
        )
    new_assigment = await assigment_collection.find_one({"_id":assigment.inserted_id})
    return assigment_helper(new_assigment)


# Retrieve all students present in the database
async def retrieve_assigments():
    assigments = []
    async for soal in assigment_collection.find():
        assigments.append(assigment_helper(soal))
    return assigments

async def retrieve_languages():
    lang = exec_code.get_languages()
    return lang

# Retrieve a assigment with a matching token_soal
async def retrieve_assigment(id: str) -> dict:
    assigment = await assigment_collection.find_one({"token_assigment": str(id)})
    if assigment:
        return assigment_helper(assigment)



# Delete a student from the database
async def delete_assigment(id: str):
    assigment = await assigment_collection.find_one({"token_assigment": str(id)})
    if assigment:
        await assigment_collection.delete_one({"token_assigment": str(id)})
        return True
