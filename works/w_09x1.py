import requests


BASE_URL = "https://reqres.in/api/users"
DATA = {"name": "Student", "job": "QA Engineer"}
header = {"x-api-key": "pub_4124d968b81b82ab2a9bc60e4c45c879b79e722b705d595aa37714bf87d9502c"}

response = requests.post(url = BASE_URL, json= DATA, headers= header)

print(f"# Created User: {response.json()["name"]}\
        Job: {response.json()["job"]}\
        Created At: {response.json()["createdAt"]}")

assert '2026' in response.json()["createdAt"]
