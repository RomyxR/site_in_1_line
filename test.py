import requests

html_content = """
<!DOCTYPE html>
<html>
<head><title>Тест</title></head>
<body>
  <h1>Привет из Python!</h1>
  <p>Этот HTML отправлен через requests.post</p>
</body>
</html>
"""

response = requests.post(
    "https://si1l.vercel.app/encode/s2",
    data=html_content,                     # ← передаём как тело запроса
    headers={"Content-Type": "text/html; charset=utf-8"}
)

print("Статус:", response.status_code)
print("Ответ:", response.json())  # потому что сервер возвращает JSON