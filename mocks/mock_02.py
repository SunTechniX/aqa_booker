import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.automationteststore.com"


@pytest.fixture
def api():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=False)
        context = browser.new_context(base_url=BASE_URL)
        api_ = context.request
        yield api_

def register_user(api_, email, password):
    url = BASE_URL + "/api/register"
    response = api_.post(url, data={"email": email, "password": password})
    return response

def register_mock(api_, mocker_):  # ← mocker — фикстура, как page или tmp_path
    # Патчим ВНУТРИ — сигнатура не меняется
    # mock_get = mocker_.patch("mocks.mock_01.playwright.sync_api.chromium.launch.context.request.post")
    mock_get = mocker_.patch.object(api_, "post")

    my_mock = mocker_.Mock()
    my_mock.json.return_value = {"user_id": 123, "email": "test@example.com"}
    my_mock.text.return_value = "Это ещё не ошибка"
    my_mock.status = 201
    my_mock.raise_for_status = mocker_.Mock()
    mock_get.return_value = my_mock


def test_mock_02(api, mocker):
    register_mock(api, mocker)
    rez = register_user(api, "Sanchez", "SuPassword$!")
    print()
    print(rez.status)
    print(rez.json())
