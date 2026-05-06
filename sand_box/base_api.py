# import requests  # -= 1 =-
from playwright.sync_api import sync_playwright

from data.booking_url_api import BASE_URL


class BaseApi:  # -= 2 =-

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.drv = None
        self.api = None
        self.start()
        self.session = self.api
        #self.session = requests.Session()

    def start(self):
        self.drv = sync_playwright().start()
        browser = self.drv.chromium.launch(headless=True)
        context = browser.new_context()
        self.api = context.request

    # def stop(self):
    #     self.drv.stop()

    def check_status_code(self, resp):
        assert resp.status == 200, "Код не 200"
        #assert resp.status_code == 200, "Код не 200"

    def get(self, endpoint):
        url_ = self.base_url + endpoint
        resp = self.session.get(url=url_)
        self.check_status_code(resp)
        return resp.json()

    def post(self, endpoint, json_):
        url_ = self.base_url + endpoint
        self.api.post(url=url_, data=json_)
        resp = self.session.post(url=url_, data=json_)
        self.check_status_code(resp)
        return resp.json()

    def close(self):
        # self.session.close()
        self.drv.stop()
