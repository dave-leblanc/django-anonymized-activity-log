import hashlib


def md5_hexdigest(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()

def sha1_hexdigest(data):
    return hashlib.sha1(data.encode('utf-8')).hexdigest()

def sha224_hexdigest(data):
    return hashlib.sha224(data.encode('utf-8')).hexdigest()

def sha256_hexdigest(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def sha384_hexdigest(data):
    return hashlib.sha384(data.encode('utf-8')).hexdigest()

def sha512_hexdigest(data):
    return hashlib.sha512(data.encode('utf-8')).hexdigest()
