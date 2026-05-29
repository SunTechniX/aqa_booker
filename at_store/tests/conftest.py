# import logging
import pytest
from playwright.sync_api import sync_playwright, Browser

from at_store.data.data_at_store import BASE_URL


@pytest.fixture
def driver():
    with sync_playwright() as drv:
        yield drv

@pytest.fixture
def context(driver):
    browser: Browser = driver.chromium.launch(headless=True)
    context = browser.new_context(base_url=BASE_URL)
    yield context
    context.close()
    browser.close()

@pytest.fixture
def page(context):
    return context.new_page()


# conftest.py
import pytest
from playwright.sync_api import Page


@pytest.fixture
def api_login(page: Page):
    """Фикстура: логинит пользователя через API и возвращает page в авторизованном состоянии"""

    def _login(email: str, password: str):
        page.goto(
            "https://www.automationteststore.com/index.php?rt=account/login")

        csrf_token = page.locator(
            "#loginFrm [name='csrftoken']").get_attribute("value")
        csrf_instance = page.locator(
            "#loginFrm [name='csrfinstance']").get_attribute("value")

        payload = {
            "csrftoken": csrf_token,
            "csrfinstance": csrf_instance,
            "loginname": email,
            "password": password,
            "account": "login"
        }

        response = page.request.post(
            "/index.php?rt=account/login",
            form=payload
        )
        assert response.ok, f"Login failed: {response.status}"

        # Обновляем страницу, чтобы браузер применил куки
        page.goto("/index.php?rt=account/account", wait_until="networkidle")
        return page

    return _login


# Использование в тесте:
def test_my_account(api_login, page):
    authorized_page = api_login("user@example.com", "pass123")
    assert authorized_page.locator("text=My Account").is_visible()
    # ... дальше тестирование ЛК


# class TestFormatter(logging.Formatter):
#     def format(self, record):
#         # Добавляем поля из extra в сообщение
#         if hasattr(record, 'user'):
#             record.msg = f"[user:{record.user}] {record.msg}"
#         if hasattr(record, 'test_id'):
#             record.msg = f"[{record.test_id}] {record.msg}"
#         return super().format(record)
#
#
# def pytest_configure(config):
#     handler = logging.StreamHandler()
#     handler.setFormatter(TestFormatter(
#         fmt="%(asctime)s [%(levelname)8s] %(name)s:%(lineno)d → %(message)s",
#         datefmt="%H:%M:%S"
#         ))
#
#     logi = logging.getLogger()
#     logi.setLevel(logging.INFO)
#     logi.addHandler(handler)
