import requests

URL = "https://reqres.in/api/login"

body = {"email": "eve.holt@reqres.in",
        "password": "pistol"}

headers = {"x-api-key": "free_user_3DQhLjkSPPgFZONnLcAhGXf9DPZ"}

response = requests.post(URL, json=body, headers=headers)
data = response.json()
print(data)
token = data.get("token")
print(f"Token: {token}")
print(f"Token Length: {len(token)}")
print(f"Status: {response.status_code}")

# Проверка
assert isinstance(token, str), "Токен не строка"
assert token != "", "Токен пустой"

print("✅ Token успешно получен")
