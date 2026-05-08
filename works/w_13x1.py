import requests


def test_1():
    response = requests.get("https://httpbin.org/headers", headers={"X-Student-Name": "Maria",
                                                                    "X-Course": "Testing"
                                                                    })
    print(response.json()["headers"]["User-Agent"])
    print(response.json()["headers"]["X-Student-Name"])

    assert response.status_code == 200
    assert response.json()["headers"]["X-Course"] == "Testing"
    assert response.json()["headers"]["X-Student-Name"] == "Maria"
