import os
import requests
from dotenv import load_dotenv
from selenium.webdriver.common.actions.interaction import NONE

from data.booking_url_api import BASE_URL, AUTH, HEADERS_DATA, BOOKING

load_dotenv()


class BaseBookApi:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.auth_token = None
        # self.auth_token = self.get_token()
        self.session = requests.Session()
        self.session.headers.update(HEADERS_DATA)

    def _check_status_code(self, code: int, expected_status_code: int = 200):
        assert code == expected_status_code, \
            f"Ожидали код {expected_status_code}, получили {code}"

    def login(self):
        url = f"{self.base_url}{AUTH}"
        data_json = {"username": os.getenv("BOOKER_NAME"),
                     "password": os.getenv("BOOKER_PASSWORD")}
        response = self.session.post(url, json=data_json)
                                     # headers=HEADERS_DATA)
        response.raise_for_status()
        self.auth_token = response.json()["token"]
        return self.auth_token

    def get(self, endpoint: str, expected_status_code: int = 200):
        url_ = f"{self.base_url}{endpoint}"
        #headers_ = HEADERS_DATA
        response = self.session.get(url=url_) #, headers=headers_)
        self._check_status_code(response.status_code, expected_status_code)
        data_res = response.json()
        return data_res

    def post(self, endpoint: str, data_json: dict = None,
             expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        url_ = f"{self.base_url}{endpoint}"
        # headers_ = HEADERS_DATA
        # headers_["Cookie"] = f"token={self.auth_token}"
        print(f"\n{data_json=}")
        # print(f"{headers_=}")
        try:
            response = self.session.post(url=url_, json=data_json)  #, headers=headers_)
        except ConnectionError as e:
            print("\n=== No Connection ===")
            raise AssertionError(e)
        self._check_status_code(response.status_code,
                                expected_status_code)
        data_res = response.json()
        return data_res

    def close(self):
        self.session.close()
