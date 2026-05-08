import requests

base_url = "https://jsonplaceholder.typicode.com/posts/1"
respons = requests.get(base_url)

assert respons.status_code == 200, f"Error :{respons.status_code}"

data = respons.json()

print(respons.status_code)
print(f"Id {data['id']}")
print(f" Title {data['title']}")

telo_zaprosa_bollee_100_simvolov = len(data['body'])
print("body", telo_zaprosa_bollee_100_simvolov)
