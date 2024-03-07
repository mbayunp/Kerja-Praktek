import motor.motor_asyncio


def codexconndb():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:123@backend_dbcode:27017/')
    db = client.codeexecdb
    dbsoal = db["assigment"]
    dbjawaban = db["answer"]
    return {
        "dbsoal": dbsoal,
        "dbjawaban": dbjawaban,
    }

def codecorrconndb():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://root:123@backend_dbcode:27017/')
    db = client.codecorrectiondb
    dbsoal = db["assigment"]
    dbjawaban = db["answer"]
    return {
        "dbsoal": dbsoal,
        "dbjawaban": dbjawaban,
    }
