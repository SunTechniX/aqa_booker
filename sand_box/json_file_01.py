import json

# Из строки в объект
text = '{"name": "Buddy", "age": 3}'
data = json.loads(text)
print(data["name"])  # → Buddy

# Из объекта в строку
output = json.dumps(data, indent=2)
print(output)
