from bson.objectid import ObjectId
from utils.devops import codexconndb
from repositories.generate_token import mkid
from controlers.codex_assigment_controler import assigment_helper
from repositories.exec_code import execute_code as exec

answer_collection = codexconndb()["dbjawaban"]
assigment_collection = codexconndb()["dbsoal"]

def answer_helper(answer) -> dict:
    return {
        "id": str(answer["_id"]),
        "answer_token": answer["answer_token"],
        "token_assigment": answer["token_assigment"],
        "id_bahasa_program":answer["id_bahasa_program"],
        "answer": answer["answer"],
        "result": answer["result"],
    }

#add answer
async def add_answer(answer_data: dict) -> dict:
    cari = await assigment_collection.find_one({"token_assigment":str(answer_data["token_assigment"])})
    if cari:
        i=0
        row_soal = assigment_helper(cari)
        result = []
        testcase = row_soal["testcase"]
        inp = row_soal["input"]
        output = row_soal["output_answer"]
        code = answer_data["answer"]
        lang = answer_data["id_bahasa_program"]
        if inp is not None:
            hasil = exec(code, lang, inp, output)
            result.append(hasil)
            if testcase is not None:
                for i in range(testcase):
                    stdin = row_soal["condition_test"][i]["input"]
                    out = row_soal["condition_test"][i]["output"]
                    hasil = exec(code, lang, stdin, out)
                    result.append(hasil)                
        else:
            hasil = exec(code, lang, None, output)
            result.append(hasil)
                
        answer = await answer_collection.insert_one(
            {
                "answer_token":mkid(), 
                "token_assigment":answer_data["token_assigment"],
                "id_bahasa_program":answer_data["id_bahasa_program"],
                "answer":answer_data["answer"],
                "result":result,
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
    async for answer in answer_collection.find({"token_assigment": str(id)}):
        all_answer.append(answer_helper(answer))
    return all_answer

