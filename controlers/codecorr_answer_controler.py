from bson.objectid import ObjectId
from utils.devops import codecorrconndb
from repositories.generate_token import mkid
import repositories.similiarCS as similiarCS
import repositories.similiarOC as similiarOC
from controlers.codecorr_assigment_controler import assigment_helper

answer_collection = codecorrconndb()["dbjawaban"]
assigment_collection = codecorrconndb()["dbsoal"]

def answer_helper(answer) -> dict:
    return {
        "id": str(answer["_id"]),
        "answer_token": answer["answer_token"],
        "assigment_token": answer["assigment_token"],
        "answer": answer["answer"],
        "result": answer["result"],
    }

#add answer
async def add_answer(answer_data: dict) -> dict:
    cari = await assigment_collection.find_one({"token_soal":str(answer_data["assigment_token"])})
    if cari:
        row_soal = assigment_helper(cari)
        err_percent_cs = row_soal["check_error"]["check_error_CS"]["err_percent"]
        err_percent_oc = row_soal["check_error"]["check_error_OC"]["err_percent"]
        cs = similiarCS.check_CS(row_soal["soal"],answer_data["answer"],err_percent_cs)
        oc = similiarOC.overlap(row_soal["soal"],answer_data["answer"],err_percent_oc)
        answer = await answer_collection.insert_one(
            {
                "answer_token":mkid(), 
                "assigment_token":answer_data["assigment_token"],
                "answer":answer_data["answer"],
                "result":{
                    "check_error_CS":cs,
                    "check_error_OC":oc,
                },
            }
            )
        new_answer = await answer_collection.find_one({"_id": answer.inserted_id})
        return answer_helper(new_answer)
    else:
        return False

#Show All Answer Data
async def retrieve_answers():
    all_answer = []
    async for answer in answer_collection.find():
        all_answer.append(answer_helper(answer))
    return all_answer

async def retrieve_answer(id: str) -> dict:
    all_answer = []
    async for answer in answer_collection.find({"assigment_token": str(id)}):
        all_answer.append(answer_helper(answer))
    return all_answer
# Retrieve a answer with a matching token_soal
#async def retrieve_answer(id: str) -> dict:
#    answers = []
#    async for answer in answer_collection.find_one()
#    answer = await answer_collection.find_one({"token_soal": str(id)})
#    if answer:
#        return assigment_helper(assigment)
