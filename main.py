from fastapi import *
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
import uvicorn
import si1l_compress
import si1l_compress2

app = FastAPI()

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    # Добавляем иконку сайта
    return FileResponse('favicon.ico')

@app.get("/")
async def main_page(): 
    # Главная страница
    return FileResponse("main_page.html")

@app.get("/c")
async def html_to_si1l_page(): 
    # Конвертер
    return FileResponse("html2si1l.html")

@app.get("/c2")
async def html_to_si1l2_page(): 
    # Конвертер
    return FileResponse("html2si1l2.html")

@app.get("/s/{si1lc_html}")
async def display_si1l_html(si1lc_html: str):
    # Декодирует строку si1l из пути URL и отображает ее как HTML.
    try:
        html_content = si1l_compress.decompress(si1lc_html)
        return HTMLResponse(html_content)
    except Exception as e:
        # Перехватываем конкретные ошибки декодирования для более информативных сообщений
        raise HTTPException(status_code=400, detail=f"Неверное содержимое si1lc или UTF-8: {e}")
    
@app.get("/s2/{si1lc2_html}")
async def display_si1l2_html(si1lc2_html: str):
    # Декодирует строку si1l2 из пути URL и отображает ее как HTML.
    try:
        html_content = si1l_compress2.decompress(si1lc2_html)
        return HTMLResponse(html_content)
    except Exception as e:
        # Перехватываем конкретные ошибки декодирования для более информативных сообщений
        raise HTTPException(status_code=400, detail=f"Неверное содержимое si1lc2 или UTF-8: {e}")


@app.post("/encode/s")
async def encode_si1l(request: Request):
    try:
        html = await request.body()
        html_str = html.decode("utf-8")
        si1l_encoded = si1l_compress.compress(html_str)  # ← должен быть метод compress
        # Возвращаем относительную ссылку (клиент сам соберёт полный URL)
        return JSONResponse({"url": f"/s/{si1l_encoded}"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка кодирования si1l: {e}")

@app.post("/encode/s2")
async def encode_si1l2(request: Request):
    try:
        html = await request.body()
        html_str = html.decode("utf-8")
        si1l2_encoded = si1l_compress2.compress(html_str)  # ← должен быть метод compress
        return JSONResponse({"url": f"/s2/{si1l2_encoded}"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Ошибка кодирования si1l2: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
 
