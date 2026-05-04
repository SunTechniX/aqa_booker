import os
import requests
from dotenv import load_dotenv

from data.api_url import BASE_URL, AUTH, HEADERS_DATA, BOOKING

load_dotenv()


class ApiClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.auth_token = None
        # self.auth_token = self.get_token()
        self.session = requests.Session()
        self.session.headers.update(HEADERS_DATA)

    def response_json_with_status(self, response, expected_status_code=200):
        status_code = response.status_code
        assert status_code == expected_status_code, \
            f"Ожидали код {expected_status_code}, получили {status_code}"
        return response.json()

    def login(self):
        url = f"{self.base_url}{AUTH}"
        json_data = {"username": os.getenv("BOOKER_NAME"),
                     "password": os.getenv("BOOKER_PASSWORD")}
        response = self.session.post(url, json=json_data,
                                     headers=HEADERS_DATA)
        response.raise_for_status()
        self.auth_token = response.json()["token"]
        return self.auth_token

    def get_token(self):
        url = f"{self.base_url}{AUTH}"
        json_data = {"username": os.getenv("BOOKER_NAME"),
                     "password": os.getenv("BOOKER_PASSWORD")}
        response = requests.post(url, json=json_data,
                                 headers=HEADERS_DATA)
        response_data = self.response_json_with_status(response)
        assert "token" in response_data, "Токен не получен"
        return response_data["token"]

    def create_booking(self, booking_data):
        url = f"{BASE_URL}{BOOKING}"
        headers_ = {"Content-Type": "application/json"}
        # headers_ = {"Content-Type": "application/json",
        #             "Cookie": f"token={self.auth_token}"}
        response = self.session.post(url, json=booking_data,
                                     headers=headers_)
        data = self.response_json_with_status(response)
        return data["bookingid"]

    def close(self):
        self.session.close()
