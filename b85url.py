import math

# Base85URL алфавит (85 безопасных символов для URL)
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~!*'()"
BASE = len(ALPHABET)  # 85

def base85url_encode(data):
    """Кодирует байты в Base85URL строку"""
    if isinstance(data, str):
        data = data.encode('utf-8')
    # Конвертируем байты в большое число
    num = int.from_bytes(data, byteorder='big')
    
    if num == 0: return ALPHABET[0]
    # Конвертируем число в Base85
    encoded = ""
    while num > 0:
        num, remainder = divmod(num, BASE)
        encoded = ALPHABET[remainder] + encoded
    
    return encoded

def base85url_decode(encoded):
    """Декодирует Base85URL строку в байты"""
    num = 0
    for char in encoded:
        num = num * BASE + ALPHABET.index(char)
    
    if num == 0: return b''
    
    byte_length = (num.bit_length() + 7) // 8
    return num.to_bytes(byte_length, byteorder='big')

# Удобные функции для строк
def encode_string(text):
    return base85url_encode(text)
def decode_string(encoded):
    return base85url_decode(encoded).decode('utf-8')  