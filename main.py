from fastapi import *
from fastapi.responses import HTMLResponse, FileResponse
import uvicorn
import b85url

app = FastAPI()

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    # Добавляем иконку сайта
    return FileResponse('favicon.ico')

@app.get("/")
async def main_page(): 
    # Главная страница
    return FileResponse("main_page.html")

@app.get("/s/{base85url_html:path}")
async def display_base85url_html(base85url_html: str):
    # Декодирует строку Base85url из пути URL и отображает ее как HTML.
    try:
        html_content = b85url.decode_string(base85url_html)
        return HTMLResponse(html_content)
    except Exception as e:
        # Перехватываем конкретные ошибки декодирования для более информативных сообщений
        raise HTTPException(status_code=400, detail=f"Неверное содержимое Base85_url или UTF-8: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
