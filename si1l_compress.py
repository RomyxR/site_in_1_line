import brotli
from bs4 import BeautifulSoup, Comment
import re
from b85url import *

def compress(text: str):
    def clean_html(html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
            comment.extract()
        return re.sub(r'>\s+<', '><', str(soup)).strip()
    
    cleaned = clean_html(text)
    compressed = brotli.compress(cleaned.encode('utf-8'), quality=11)
    return base85url_encode(compressed)

def decompress(encoded_text: str):
    decoded = base85url_decode(encoded_text)
    decompressed = brotli.decompress(decoded)
    return decompressed.decode('utf-8')

def decompress_safe(encoded_text: str):
    decoded = base85url_safe_decode(encoded_text)
    decompressed = brotli.decompress(decoded)
    return decompressed.decode('utf-8')

def compress_safe(text: str):
    def clean_html(html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        for comment in soup.find_all(string=lambda t: isinstance(t, Comment)):
            comment.extract()
        return re.sub(r'>\s+<', '><', str(soup)).strip()
    
    cleaned = clean_html(text)
    compressed = brotli.compress(cleaned.encode('utf-8'), quality=11)
    return base85url_safe_encode(compressed)




# Тестовые данные
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
    original_len = len(test)
    compressed_encoded = compress(test)
    compressed_len = len(compressed_encoded)
    restored = decompress(compressed_encoded)
    restored_len = len(restored)

    print("Original length:", original_len)
    print("Compressed (Brotli + base85url) length:", compressed_len)
    print("Restored length:", restored_len)
    print("Equal?", test == restored)