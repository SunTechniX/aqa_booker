import requests  # -= 1 =-

from data.booking_url_api import BASE_URL


class BaseApi:  # -= 2 =-

    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        url_ = self.base_url + endpoint
        resp = self.session.get(url=url_)
        assert resp.status_code == 200, "Код не 200"
        return resp.json()

    def post(self, endpoint, json_):
        url_ = self.base_url + endpoint
        resp = self.session.post(url=url_, json=json_)
        assert resp.status_code == 200, "Код не 200"
        return resp.json()

    def close(self):
        self.session.close()
