import uuid
import hashlib
def get_token():
    u_token = uuid.uuid4()
    u_str = str(u_token).encode("utf-8")

    md5 = hashlib.md5()
    md5.update(u_str)
    return md5.hexdigest()
