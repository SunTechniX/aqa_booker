import requests
import time

url = "https://httpbin.org/delay/2"

try:
    start = time.time()
    response = requests.get(url, timeout=5)
    duration = round(time.time() - start, 1)


    assert response.status_code == 200

    print(f"Request Time: {duration}")
    print(f"Status: OK")
    print(f"Delayed: {duration > 1.5}")

except requests.exceptions.Timeout:
    print("TimeoutError: запрос превысил 5 секунд")
