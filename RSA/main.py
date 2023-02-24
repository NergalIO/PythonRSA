from RSA.env import RSA, code

def CreateInstance(*args, **kwargs) -> RSA:
    return RSA(*args, **kwargs)

def generate(instance: RSA) -> None:
    instance.generate()

def encode(instance: RSA, text: str) -> bytes:
    encoded = instance.encode(code(text))
    return f'{len(encoded)}854367{int.from_bytes(encoded, "big")}'

def decode(instance: RSA, text: str) -> str:
    sizeof, payload = text.split('854367')
    return code(instance.decode(int(payload).to_bytes(int(sizeof), "big")))

def file_encrypt(instance: RSA, bytes: bytes, filepath: str) -> None:
    from random import randbytes
    
    payload = instance.encode(bytes)
    zeros = randbytes(1024 * (len(payload) % 1024) - len(payload))
    with open(filepath, "wb") as file:
        file.write(len(zeros).to_bytes(4, "big") + payload + zeros)

def file_decrypt(instance: RSA, fulldata: bytes, filepath: str) -> None:
    sizeof = int.from_bytes(fulldata[:4], "big")
    payload = fulldata[4:len(fulldata) - sizeof]
    with open(filepath, "wb") as file:
        file.write(instance.decode(payload))

def get_keys(instance: RSA) -> str:
    return instance.get_keys()


def prepare_keys(instance: RSA) -> bytes:
    return instance.prepare_keys()

def import_keys(instance: RSA, keys: bytes) -> None:
    instance.import_keys(keys)
