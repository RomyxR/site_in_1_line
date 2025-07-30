ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~!*'()"
BASE = len(ALPHABET)

def base85url_encode(data):
    if isinstance(data, str): data = data.encode('utf-8')
    num = int.from_bytes(data, 'big')
    encoded = ""
    while num > 0:
        num, remainder = divmod(num, BASE)
        encoded = ALPHABET[remainder] + encoded
    return encoded

def base85url_decode(encoded):
    num = sum(ALPHABET.index(char) * BASE**i for i, char in enumerate(reversed(encoded)))
    return num.to_bytes((num.bit_length() + 7) // 8, 'big')

def encode_string(text):
    return base85url_encode(text)
def decode_string(encoded):
    return base85url_decode(encoded).decode('utf-8')  
