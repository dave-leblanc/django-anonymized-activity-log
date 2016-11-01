import hashlib


def md5_hexdigest(data):
    return hashlib.md5(data).hexdigest()

# TODO: add more crypto types
