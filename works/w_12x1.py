import requests


data = {
    "task": "API testing",
    "priority": "high",
    "points": 100
}

response = requests.post("https://httpbin.org/post", json=data)

res_json = response.json()

task = res_json['json']['task']
priority = res_json['json']['priority']
points = res_json['json']['points']

print(f"Task: {task}")
print(f"Priority: {priority}")
print(f"Points: {points}")

if points == 100:
    print("Проверка пройдена: Points равно 100")
else:
    print("Ошибка: Points не равно 100")
