import uuid
import hashlib

def myutil_get_token():
    u_uuid = uuid.uuid4()
    u_str = str(u_uuid.encode('utf-8'))

    md5 = hashlib.md5()
    md5.update(u_str)
    return md5.hexdiges