import base64

def encode(unencoded: str):
    tempunencoded = unencoded.encode("ascii")
    base64_bytes = base64.b64encode(tempunencoded)
    return base64.b64encode(tempunencoded).decode("ascii")

def decode(undecoded: str):
    undecoded_string = undecoded.encode("ascii")
    return base64.b64decode(undecoded_string).decode("ascii")
