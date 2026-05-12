import requests


def test_2():
    response_2 = requests.get("https://httpbin.org/headers", headers={
        "Authorization": "Bearer test-token-123",
        "X-Student-ID": "999"
        })
    print(response_2.json()["headers"]["Authorization"])
    print(response_2.json()["headers"]["X-Student-Id"])

    assert response_2.status_code == 200
    assert response_2.json()["headers"][
               "Authorization"] == "Bearer test-token-123"
    assert response_2.json()["headers"]["X-Student-Id"] == "999"
