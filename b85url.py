ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~!*'()"
SAFE_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"
BASE = len(ALPHABET)
SAFE_BASE = len(SAFE_ALPHABET)

def base85url_encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    num = int.from_bytes(data, 'big')
    if num == 0:
        return ALPHABET[0]
    encoded = ""
    while num > 0:
        num, remainder = divmod(num, BASE)
        encoded = ALPHABET[remainder] + encoded
    return encoded

def base85url_decode(encoded):
    if not encoded:
        return b""
    num = sum(ALPHABET.index(char) * (BASE ** i) for i, char in enumerate(reversed(encoded)))
    byte_length = (num.bit_length() + 7) // 8
    return num.to_bytes(byte_length or 1, 'big')

def base85url_safe_encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    num = int.from_bytes(data, 'big')
    if num == 0:
        return SAFE_ALPHABET[0]
    encoded = ""
    while num > 0:
        num, remainder = divmod(num, SAFE_BASE)
        encoded = SAFE_ALPHABET[remainder] + encoded
    return encoded

def base85url_safe_decode(encoded):
    if not encoded:
        return b""
    num = sum(SAFE_ALPHABET.index(char) * (SAFE_BASE ** i) for i, char in enumerate(reversed(encoded)))
    byte_length = (num.bit_length() + 7) // 8
    return num.to_bytes(byte_length or 1, 'big')