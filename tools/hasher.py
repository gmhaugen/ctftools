import hashlib

def hashmd5(input: str):
    return hashlib.md5(input.encode("ascii")).hexdigest()

def hashsha1(input: str):
    return hashlib.sha1(input.encode("ascii")).hexdigest()

def hashsha224(input: str):
    return hashlib.sha224(input.encode("ascii")).hexdigest()

def hashsha256(input: str):
    return hashlib.sha256(input.encode("ascii")).hexdigest()

def hashsha384(input: str):
    return hashlib.sha384(input.encode("ascii")).hexdigest()

def hashsha512(input: str):
    return hashlib.sha512(input.encode("ascii")).hexdigest()

def hashsha3_224(input: str):
    return hashlib.sha3_224(input.encode("ascii")).hexdigest()

def hashsha3_256(input: str):
    return hashlib.sha3_256(input.encode("ascii")).hexdigest()

def hashsha3_384(input: str):
    return hashlib.sha3_384(input.encode("ascii")).hexdigest()

def hashsha3_512(input: str):
    return hashlib.sha3_512(input.encode("ascii")).hexdigest()