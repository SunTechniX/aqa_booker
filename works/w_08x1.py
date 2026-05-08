import requests

URL = "https://reqres.in/api/users?page=2"
headers_ = {"x-api-key": "pub_4124d968b81b82ab2a9bc60e4c45c879b79e722b705d595aa37714bf87d9502c"}

response = requests.get(url=URL, headers=headers_)

response_data = response.json()
page = response_data["page"]
total_pages = response_data["total_pages"]
first_user_name = response_data["data"][0]["first_name"]
print(f"Page: {page}")
print(f"Total Pages: {total_pages}")
print(f"First User on Page: {first_user_name}")

assert len(response_data["data"]) == 6
