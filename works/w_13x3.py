import requests


def test_3():
    session = requests.Session()
    response_1 = session.get(
        "https://httpbin.org/cookies/set?student=ivan&course=api"
    )

    print(f"[SET] student: {response_1.json()['cookies']['student']}")
    print(f"[SET] course: {response_1.json()['cookies']['course']}")

    response_2 = session.get("https://httpbin.org/cookies")
    cookies = response_2.json()["cookies"]

    print(f"[GET] Cookies Count: {len(cookies)}")
    print(f"[VERIFY] student in cookies: {'student' in cookies}")

    assert cookies["student"] == "ivan"
    assert cookies["course"] == "api"
