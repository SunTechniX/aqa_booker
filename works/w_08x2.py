import requests

URL = "https://reqres.in/api/users"
headers_ = {"x-api-key": "pub_4124d968b81b82ab2a9bc60e4c45c879b79e722b705d595aa37714bf87d9502c"}
data_json = {"name": "New Student", "job": "API Tester"}

response = requests.post(url=URL, json=data_json, headers=headers_)
json_response = response.json()

print(f'Created User: {json_response['name']}')
print(f'Job: {json_response['job']}')
year = json_response["createdAt"]
print(f'Сreated At: {year}')
assert year[:4] == "2026", "Год не совпадает"
