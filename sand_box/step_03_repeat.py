import os
import pytest
import requests
from dotenv import load_dotenv
from gprof2dot import PRINT_COLORMAP

load_dotenv()

HEADERS_DATA = {"Content-Type": "application/json",
                "Accept": "application/json"}
BASE_URL = "https://restful-booker.herokuapp.com"
AUTH = "/auth"
BOOKING = "/booking"
BOOKING_DATA = {
    "firstname": "Миша",
    "lastname": "Газонов",
    "totalprice": 1110,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-05-06",

        "checkout": "2026-06-14"
    },
    "additionalneeds": "Breakfast"
}

BOOKING_DATA_PUT = {
    "firstname": "Андрей",
    "lastname": "Филлимонов",
    "totalprice": 121212,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-05-12",
        "checkout": "2026-10-10"
    },
    "additionalneeds": "Tea"
}

@pytest.fixture(scope="session")
def my_sess():
    sess = requests.Session()
    url = f"{BASE_URL}{AUTH}"
    data_json = {"username": os.getenv("BOOKER_NAME"),
                 "password": os.getenv("BOOKER_PASSWORD")}
    response = sess.post(url, json=data_json)
    response.raise_for_status()
    auth_token = response.json()["token"]
    HEADERS_DATA['Cookie'] = f"token={auth_token}"
    sess.headers.update(HEADERS_DATA)
    print("Сессия Создана")
    yield sess
    print("Сессия закрылась")
    sess.close()


class TestStep_03:
    ID = None

    def test_01(self, my_sess):
        url = f"{BASE_URL}{BOOKING}"
        response = my_sess.post(url, json=BOOKING_DATA)
        data_json = response.json()
        TestStep_03.ID = data_json.get("bookingid")
        print(f"2: {data_json=}")

    def test_02(self, my_sess):
        url = f"{BASE_URL}{BOOKING}/{TestStep_03.ID}"
        print(f"{TestStep_03.ID=}")
        response = my_sess.put(url, json=BOOKING_DATA_PUT)
        response.raise_for_status()
        print(f"3: {response.json()=}")

