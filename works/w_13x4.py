import requests


def test_4():
    response_1 = requests.get(
        "https://httpbin.org/headers", headers={
            "X-Test-String": "hello",
            "X-Test-Number": "123",
            "X-Test-Boolean": "true"
        }
    )

    assert response_1.status_code == 200
    assert response_1.json()["headers"]["X-Test-String"] == "hello"
    assert response_1.json()["headers"]["X-Test-Number"] == "123"
    assert response_1.json()["headers"]["X-Test-Boolean"] == "true"

    all_headers_match = (
            response_1.json()["headers"]["X-Test-String"] == "hello"
            and response_1.json()["headers"]["X-Test-Number"] == "123"
            and response_1.json()["headers"]["X-Test-Boolean"] == "true"
    )

    print("[SENT] X-Test-String: hello")
    print(f"[ECHOED] X-Test-String: {response_1.json()['headers']['X-Test-String']}")
    print(f"[MATCH] All headers echoed: {all_headers_match}")
