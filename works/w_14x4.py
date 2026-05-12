import requests

res_200 = requests.get("https://httpbin.org/status/200")
res_400 = requests.get("https://httpbin.org/status/400")
res_503 = requests.get("https://httpbin.org/status/503")

match_200 = res_200.status_code == 200
match_400 = res_400.status_code == 400
match_503 = res_503.status_code == 503

body_400 = len(res_400.content) > 0
body_503 = len(res_503.content) > 0

if match_200 == True and match_400 == True and match_503 == True:
    all_valid = True
else:
    all_valid = False

print(f"[200] Status match: {match_200}")
print(f"[400] Status match: {match_400}, Body present: {body_400}")
print(f"[503] Status match: {match_503}, Body present: {body_503}")
print(f"[RESULT] All status codes valid: {all_valid}")