import requests
import time


url2 = "https://httpbin.org/delay/3"
start_total = time.time()

try:
    requests.get(url2, timeout=2)
except requests.exceptions.Timeout:
    print("Attempt 1: Timeout")

    requests.get(url2, timeout=5)
    print("Attempt 2: Success")

    total_time = round(time.time() - start_total, 1)
    print(f"Total Time: {total_time}")
