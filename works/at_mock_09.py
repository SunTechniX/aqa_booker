from unittest.mock import patch, Mock

import requests


BASE_URL = "https://www.automationteststore.com/"
AUTH = "/api/register"
DATA = {"user_id": 100, "email": "test100@example.com"}
EMAIL = "test100@example.com"
PASSWORD = 12345

def register_user(email, password):
    response = requests.post(url = BASE_URL + AUTH, json= DATA)
    response.raise_for_status()
    status = response.status_code
    body = response.json()
    return status, body


def test_mock_01():
    with patch("works.at_mock_09.requests.post") as mock_get:
        my_mock = Mock()
        my_mock.status_code = 201
        my_mock.json.return_value = {"user_id": 123, "email": "test@example.com"}
        my_mock.raise_for_status = Mock()
        mock_get.return_value = my_mock

        status, body = register_user(EMAIL, PASSWORD)
        print(f"{status=}, {body=}")
        assert status == 201
        assert body == {"user_id": 123, "email": "test@example.com"}


def test_email_already_exists():
    with patch("works.at_mock_09.requests.post") as mock_post:
        my_mock = Mock()
        my_mock.status_code = 400
        my_mock.json.return_value = {"message": "Email already exists"}
        mock_post.return_value = my_mock

        status, body = register_user(EMAIL, PASSWORD)
        assert status == 400
        assert body == {"message": "Email already exists"}
