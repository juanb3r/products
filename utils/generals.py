import hashlib


def md5_encrypt(data: str):
    data_encrypt = hashlib.md5(data.encode())
    data_encrypt_hex = data_encrypt.hexdigest()
    return data_encrypt_hex
