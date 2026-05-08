import requests

URL = "https://reqres.in/api/register"

headers = {
    "x-api-key": "free_user_3DQhLjkSPPgFZONnLcAhGXf9DPZ"
}

body = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

response = requests.post(URL, json=body, headers=headers)

print(response.status_code)

data = response.json()
print(data)

token = data["token"]

print(f"Token: {token}")
print(f"Token Length: {len(token)}")

assert isinstance(token, str)
assert token != ""

print("Токен успешно проверен ✅")
