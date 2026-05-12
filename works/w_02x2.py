# import urllib.request
# import json
#
# url = "https://jsonplaceholder.typicode.com/comments?postId=1"
#
# response = urllib.request.urlopen(url)
#
# data = json.loads(response.read())
#
# print("Post ID:", data[0]["postId"])
# print("Comments Count:", len(data))
# print("First Comment Email:", data[0]["email"])
#
# for comment in data:
#     assert comment["postId"] == 1
#
# print("все комментарии имеют postId == 1")


import requests

session = requests.Session()

url = "https://jsonplaceholder.typicode.com/comments?postId=1"

response = session.get(url)

data = response.json()

print("Post ID:", data[0]["postId"])
print("Comments Count:", len(data))
print("First Comment Email:", data[0]["email"])

for comment in data:
    assert comment["postId"] == 1

print("все комментарии имеют postId == 1")

session.close()

