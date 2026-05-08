import requests

API_KEY = "free_user_3DQfOrPl1zlJWvE4MjfkWmYULs8"
url = "https://reqres.in/api/users/2"
headers = {
    "x-api-key": API_KEY
}

response = requests.get(url, headers=headers)

data = response.json()

user = data['data']

print(data)

avatar = user['avatar']
trunc_avatar = avatar[:40]

print(f"User ID: {user['id']}")
print(f"Email: {user['email']}")
print(f"First Name: {user['first_name']}")
print(f"Avatar: {trunc_avatar}")

email_contains = 'reqres.in' in user['email']
print(f"Email contains reqres.in: {email_contains}")
