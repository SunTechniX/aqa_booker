import requests

BASE_URL = "https://www.automationteststore.com"

def send_order_confirmation(email, order_id):
    return f"Sended {order_id} on {email}"

def sender_mock(mocker_):
    mock_get = mocker_.patch.object(requests__, "post"__)

    my_mock = mocker_.Mock()
    my_mock.json.return_value = {"user_id": 123, "email": "test@example.com"}
    my_mock.status_code = 201
    my_mock.raise_for_status = mocker_.Mock()
    mock_get.return_value = my_mock

def test_mock_03(mocker):
    sender_mock(mocker)
    rez = send_order_confirmation("Sanchez@mail.ru", "5555")
