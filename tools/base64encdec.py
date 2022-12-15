import base64

def encode(unencoded: str):
    return base64.b64encode(unencoded.encode("ascii")).decode("ascii")

def decode(undecoded: str):
    return base64.b64decode(undecoded.encode("ascii")).decode("ascii")
