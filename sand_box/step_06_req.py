from jsonschema import validate
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL_ = "https://restful-booker.herokuapp.com"
AUTH = "/auth"
BOOKING = "/booking"
BOOKING_DATA = {
    "firstname": "Миша",
    "lastname": "Галустьян",
    "totalprice": 3333,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2026-05-08",
        "checkout": "2026-06-17"
    },
    "additionalneeds": "Meat"
}


BOOKING_SCHEMA = {
    "type": "object",
    "required": ["firstname", "lastname", "totalprice",
                 "depositpaid", "bookingdates"],
    "properties": {
        "firstname": {"type": "string", "minLength": 1},
        "lastname": {"type": "string"},
        "totalprice": {"type": "integer", "minimum": 0},
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "required": ["checkin", "checkout"],
            "properties": {
                "checkin": {"type": "string", "format": "date"},
                "checkout": {"type": "string", "format": "date"}
            }
        },
        "additionalneeds": {"type": ["string", "null"]}
    },
    "additionalProperties": False
}

SUPER_BOOKING_SCHEMA = {
    "type": "object",
    "required": ["bookingid", "booking"],
    "properties": {
        "bookingid": {"type": "integer", "minimum": 0},
        "booking": BOOKING_SCHEMA
    },
    "additionalProperties": False
}


class BookingDates(BaseModel):
    checkin: str
    checkout: str

class BookingModel(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str

    def my_func(self):
        pass

class SuperBookingModel(BaseModel):
    bookingid: int
    booking: BookingModel

url = f"{BASE_URL_}{AUTH}"
auth_data_json = {"username": os.getenv("BOOKER_NAME"),
             "password": os.getenv("BOOKER_PASSWORD")}
resp = requests.post(url, json=auth_data_json)
token = resp.json()["token"]

url = f"{BASE_URL_}{BOOKING}"
headers = {"Cookie": f"token={token}"}
resp = requests.post(url, headers=headers, json=BOOKING_DATA)
getted_json = resp.json()

# validate(getted_json["booking"], BOOKING_SCHEMA)
# validate(getted_json, SUPER_BOOKING_SCHEMA)
book1 = SuperBookingModel.model_validate(getted_json)
print(getted_json)
print(book1.bookingid)
print(book1.booking.bookingdates.checkin)
# print(getted_json["booking"]["firstname"])
