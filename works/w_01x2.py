import requests

new_post = {
    "userId": 1,
"title": "My New Post",
"body": "This is a test post"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts",
                         json=new_post)

data = response.json()

print(f"Created Post ID: {data['id']}")
print(f"Title: {data['title']}")
print(f"Status: {response.status_code}")

assert isinstance(data['id'], int), "ID не число"
assert data['title'] == new_post['title'], "Title не совпадает"
print("Все проверки пройдены!")
