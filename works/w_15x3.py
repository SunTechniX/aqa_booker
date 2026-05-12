import requests
import time

url = "https://httpbin.org"
successful = 0
start = time.time()

for _ in range(10):
    resp = requests.get(url)
    if resp.status_code == 200:
        successful += 1
    time.sleep(0.1)

total = round(time.time() - start, 2)
avg_time = round(total / 10, 2)

print(f"Requests Sent: 10")
print(f"Successful: {successful} 200-ок")
print(f"Failed: {10 - successful}")
print(f"Total Time: {total}")
print(f"Avg per Request: {avg_time}")

assert successful == 10
