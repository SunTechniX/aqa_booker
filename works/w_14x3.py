import requests


url_redirect = "https://httpbin.org/redirect/2"

res_follow = requests.get(url_redirect, allow_redirects=True)
res_no_follow = requests.get(url_redirect, allow_redirects=False)

print(f"[FOLLOW] Final Status: {res_follow.status_code}")
print(f"[NO-FOLLOW] Status: {res_no_follow.status_code}")
print(f"[REDIRECTS] Count: {len(res_follow.history)}")
