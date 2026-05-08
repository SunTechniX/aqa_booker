import requests

url = "https://reqres.in/api/login"
payload = {
    "email": "eve.holt@reqres.in",  # ✅ Только фикстуры из доки!
    "password": "pistol"
}

response = requests.post(url, json=payload)
print(response.status_code)  # 200
print(response.json())       # {"token": "QpwL5tke4Pnpja7X4"}
