'''📌 Задание 08 (Reqres — Список пользователей)
Ресурс: https://reqres.in/api/users?page=2

Задача:

Отправьте GET-запрос для получения второй страницы списка пользователей
Выведите в консоль:
Page: 2
Total Pages: <значение поля total_pages>
First User on Page: <имя первого пользователя в массиве data>


Проверьте, что в ответе ровно 6 пользователей (поле data)

URL = "https://reqres.in/api/users?page=2"

response = requests.get(URL)'''

from dotenv import load_dotenv
import os
import requests

load_dotenv()

BASE_URL = "https://reqres.in/api"
EP_LOGIN = "/login"
EP_USERS = "/users"
SESSION_TOKEN = os.getenv("TOKEN")
# HEADERS = {"Authorization": f"Bearer {SESSION_TOKEN}",
#             "Content-Type": "application/json"}

API_KEY = "free_user_3DQfOrPl1zlJWvE4MjfkWmYULs8"
HEADERS = {
    "x-api-key": API_KEY
}

url = BASE_URL + EP_LOGIN
playload = {"email": "eve.holt@reqres.in", "password": "pistol"}
print(url)
url = f"{BASE_URL}/app/collections/:slug/records"
resp = requests.get(BASE_URL + EP_USERS, headers=HEADERS)
# resp = requests.post(url, json=playload)
print(resp.status_code)
print(resp.json())
# print("\n".join([str(item) for item in resp.json()]))
