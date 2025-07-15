from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import base64
import uvicorn

app = FastAPI()

@app.get("/")
async def main_page():
    main_page_html = """<!DOCTYPE html>
    <html lang="ru">
    <head>
    <meta charset="UTF-8">
    <title>site-in-1-line</title>
    <style>
    body {
	font-family: Arial, Helvetica, sans-serif;
    }
    </style>
    </head>
    <body>
    <h1>site-in-1-line</h1>
    <h2>Сервис для хостинга простых сайтов без хостинга. Весь сайт сохраняеться в 1 строке.</h2>
    <h2>Ваш сайт должен быть сохранён только в 1 файле HTML со встроеным CSS и JavaScript кодом.</h2>
    <h2>Закодируйте HTML в Base64, ссылка будет выглядить так: https://site-in-1-line.vercel.app/<ваш Base64 код></h2>
    </body>
    </html>
    """
    return HTMLResponse(content=main_page_html)

@app.get("/{base64_html:path}")
async def display_base64_html(base64_html: str):
    """
    Декодирует строку Base64 из пути URL и отображает ее как HTML.
    """
    try:
        # Декодируем строку Base64 напрямую
        decoded_bytes = base64.b64decode(base64_html)
        
        # Предполагаем, что декодированное содержимое является HTML в кодировке UTF-8
        html_content = decoded_bytes.decode('utf-8')
        
        return HTMLResponse(content=html_content)
    except Exception as e:
        # Перехватываем конкретные ошибки декодирования для более информативных сообщений
        raise HTTPException(status_code=400, detail=f"Неверное содержимое Base64 или UTF-8: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
