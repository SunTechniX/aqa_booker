import requests

res = requests.get("https://jsonplaceholder.typicode.com/photos/50")
assert res.status_code == 200, f"Статус 200 {res.status_code}"

photo = res.json()

print(f"Photo ID: {photo['id']}")
print(f"Title: {photo['title']}")
print(f"URL:{photo['url'][:50]}")