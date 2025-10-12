import gzip

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~!*'()"
BASE = len(ALPHABET)

def base85url_encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    num = int.from_bytes(data, 'big')
    if num == 0:
        return ALPHABET[0]  # Обработка пустых или нулевых данных
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

def compress(text: str):
    compressed = gzip.compress(text.encode('utf-8'), mtime=0)
    return base85url_encode(compressed)

def decompress(text: str):
    decoded = base85url_decode(text)
    return gzip.decompress(decoded).decode('utf-8')



test = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тестовый сайт</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #333;
        }
        .btn {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 20px 0;
            cursor: pointer;
            border: none;
            border-radius: 5px;
        }
        .btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Добро пожаловать на тестовый сайт!</h1>
    <p>Это простой пример веб-страницы для тестирования.</p>
    <button class="btn" onclick="alert('Тест пройден!')">Нажми меня</button>
</body>
</html>"""

if __name__ == "__main__":
    print("Original:", len(test))
    print("Compressed:", len(compress(test)))
    print("Restored:", len(decompress(compress(test))))
    print("encode b86url", len(base85url_encode(test)))
    print("Equal?", test == decompress(compress(test)))