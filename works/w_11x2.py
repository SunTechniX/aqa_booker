import requests


BASE_URL = "https://httpbin.org/post"
DATA = {"student": "Ivan", "course": "API", "grade": "A"}


def test_002():
    response = requests.post(url=BASE_URL, data=DATA)
    response_data = response.json()
    print(response.json())
    print(f"Student: {response_data['form']['student']}")
    print(f"Course: {response_data['form']['course']}")
    print(f"Grade: {response_data['form']['grade']}")

    assert response_data["form"]["student"] == "Ivan"
    assert response_data["form"]["course"] == "API"
    assert response_data["form"]["grade"] == "A"
