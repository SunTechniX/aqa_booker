import pytest
from playwright.sync_api import sync_playwright, Browser

from at_store.data.data_at_store import BASE_URL


@pytest.fixture
def driver():
    with sync_playwright() as drv:
        yield drv

@pytest.fixture
def context(driver):
    browser: Browser = driver.chromium.launch(headless=False)
    context = browser.new_context(base_url=BASE_URL)
    yield context
    context.close()
    browser.close()

@pytest.fixture
def page(context):
    return context.new_page()
