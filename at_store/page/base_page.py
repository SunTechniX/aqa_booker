from playwright.sync_api import Page
from at_store.data.data_at_store import BASE_URL


class BasePage:

    def __init__(self, page_):
        self.page: Page = page_

    def open(self, url="/"):
        self.page.goto(url)
