import requests

url = "https://jsonplaceholder.typicode.com/comments/5"

response = requests.get(url)

data = response.json()

print("Comment ID:", data["id"])
print("Email:", data["email"])
print("Post ID:", data["postId"])


assert "@" in data["email"]

print ("email содержит символ @")