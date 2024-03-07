import uuid, shortuuid

def mkid():
    uid = uuid.uuid4()
    s = shortuuid.encode(uid)
    shortid = s[:7]
    return shortid