from playwright.sync_api import Page, expect
from at_store.data.data_at_store import BASE_URL_NO_WWW


class BasePage:

    def __init__(self, page_):
        self.page: Page = page_

    def open(self, url="/"):
        self.page.goto(url)

    def check_url(self, endpoint="/index.html"):
        expect(self.page).to_have_url(BASE_URL_NO_WWW + endpoint)
