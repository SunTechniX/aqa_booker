import requests

BASE_URL = "https://reqres.in/api/users"
HEADER = {"x-api-key": "pub_4124d968b81b82ab2a9bc60e4c45c879b79e722b705d595aa37714bf87d9502c"}
ID = 2

response = requests.delete(url = f"{BASE_URL}/{ID}", headers= HEADER)
print(f"Deleted User ID: {ID}\n"
      f"Status Code: {response.status_code}\n"
      f"Response Body: {response}")
