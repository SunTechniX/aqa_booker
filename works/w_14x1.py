import requests

BASE_URL = "https://httpbin.org/status/201"
response = requests.get(BASE_URL)
status_code = response.status_code
status_text = response.reason
success_code = status_code in range(200, 300)

print(f"Status Code: {status_code}")
print(f"Status Text: {status_text}")
print(f"Success: {success_code}")
