from bson.objectid import ObjectId
from utils.devops import codecorrconndb
import repositories.generate_soal as generate_soal
import repositories.similiarCS as similiarCS
import repositories.similiarOC as similiarOC
import repositories.modclass
from repositories.generate_token import mkid
import repositories.exec_code as exec_code



assigment_collection = codecorrconndb()["dbsoal"]

def assigment_helper(assigment) -> dict:
    return {
        "id": str(assigment["_id"]),
        "token_soal": assigment["token_soal"],
        "soal": assigment["soal"],
        "id_bahasa_program": assigment["id_bahasa_program"],
        "idx_error": assigment["idx_error"],
        "soal_err": assigment["soal_err"],
        "output": assigment["output"],
        "check_error":assigment["check_error"]
        
    }



# Add a new student into to the database
async def add_assigment(assigment_data: dict) -> dict:
    if assigment_data["id_bahasa_program"]=='0':
        output = None
    else:
        output =  exec_code.execute_program(assigment_data["soal"],assigment_data["id_bahasa_program"])
    soal_err = generate_soal.run(assigment_data["soal"],assigment_data["idx_error"])
    cs = similiarCS.check_CS(assigment_data["soal"],soal_err,0)
    oc = similiarOC.overlap(assigment_data["soal"],soal_err,0)
    assigment = await assigment_collection.insert_one(
        {
            "token_soal":mkid(),
            "soal":assigment_data["soal"],
            "id_bahasa_program": assigment_data["id_bahasa_program"],
            "idx_error": assigment_data["idx_error"],
            "soal_err": soal_err,
            "output": output,
            "check_error": {
                "check_error_CS":cs,
                "check_error_OC":oc,
            }
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
    assigment = await assigment_collection.find_one({"token_soal": str(id)})
    if assigment:
        return assigment_helper(assigment)


# Update a Assigment with a matching ID
async def generate_assigment(id:str):
    query = {'token_soal':str(id)}
    new_data = { '$set': { 'idx_error': 5}}
    update = await assigment_collection.update_one(query,new_data)
    if update:
        return True
    return False
    # assigment = await assigment_collection.find_one({"token_soal": str(id)})
    # if assigment:
    #     row = assigment_helper(assigment)
    #     soal = row["soal"]
    #     idx = row["idx_error"]
    #     soal_err = generate_soal.run(soal,idx) 
    #     updated_assigment = await assigment.update_one(
    #         {"idx_error":row["idx_error"]},{ "$set": { "idx_error": idx } }
    #     )
    #     if updated_assigment:
    #         return True
    #     else:
    #         return False


# Delete a student from the database
async def delete_assigment(id: str):
    assigment = await assigment_collection.find_one({"token_soal": str(id)})
    if assigment:
        await assigment_collection.delete_one({"token_soal": str(id)})
        return True
