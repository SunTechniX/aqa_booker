import requests

BASE_URL = "https://www.automationteststore.com"

def register_user(email, password):
    url = BASE_URL + "/api/register"
    response = requests.post(url, data={"email": email, "password": password})
    return response

def register_mock(mocker_):  # ← mocker — фикстура, как page или tmp_path
    # Патчим ВНУТРИ — сигнатура не меняется
    # mock_get = mocker_.patch("mocks.mock_01.requests.post")
    mock_get = mocker_.patch.object(requests, "post")

    my_mock = mocker_.Mock()
    my_mock.json.return_value = {"user_id": 123, "email": "test@example.com"}
    my_mock.status_code = 201
    my_mock.raise_for_status = mocker_.Mock()
    mock_get.return_value = my_mock

def get_product(product_id):
    url = f"BASE_URL/api/product/{product_id}"
    response = requests.get(url)
    return response

def product_mock(mocker_):
    pr1 = mocker_.Mock()
    pr1.json.return_value = {"id": 1, "title": "Продукт 1"}

    pr2 = mocker_.Mock()
    pr2.json.return_value = {"id": 2, "title": "Продукт 2"}

    mocker_.patch.object(requests, "get", side_effect=[pr1, pr2])

def test_mock_01(mocker):
    register_mock(mocker)
    rez = register_user("Sanchez", "SuPassword$!")
    print("\n", rez.status_code)
    print(rez.json())

def test_mock_02(mocker):
    product_mock(mocker)
    res1 = get_product(1)
    res2 = get_product(2)
    print()
    print(res1.json())
    print(res2.json())
