from jsonschema import validate, ValidationError
from playwright.sync_api import sync_playwright, APIRequestContext
from pydantic import BaseModel, Field, ValidationError
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"
DATA_BOOK = {"firstname": "Alex", "lastname": "Test", "totalprice": 150,
             "depositpaid": True,
             "bookingdates": {"checkin": "2026-05-01",
                              "checkout": "2026-05-05"},
             "additionalneeds": "WiFi"}

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

REAL_JSON = {'bookingid': 427,
             'booking': {'firstname': 'Alex',
                         'lastname': 'Test',
                         'totalprice': 150,
                         'depositpaid': True,
                         'bookingdates': {'checkin': '2026-05-01',
                                          'checkout': '2026-05-05'},
                         'additionalneeds': 'WiFi'}
             }


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingModel(BaseModel):
    firstname: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    totalprice: int = Field(ge=0)
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str | None


@pytest.fixture(scope="module")
def context():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=True)
        context_ = browser.new_context()
        yield context_
        context_.close()
        browser.close()


def assert_schema(response_json: dict, schema: dict, step_name: str = "Schema validation"):
    """ Валидирует ответ по схеме, выдаёт понятную ошибку при провале """
    try:
        validate(instance=response_json, schema=schema)
    except ValidationError as e:
        path = " → ".join(str(p) for p in e.absolute_path) or "root"
        pytest.fail(f"❌ {step_name} failed at '{path}': {e.message}")


def assert_schema_pydantic(response_json: dict):
    """ Валидирует ответ по схеме, выдаёт понятную ошибку при провале """
    book_model = BookingModel.model_validate(response_json)
    print(book_model.firstname, book_model.lastname)


def test_create_booking_via_context(context):
    api: APIRequestContext = context.request

    # 1️⃣ Auth
    auth = api.post(f"{BASE_URL}/auth",
                    data={"username": "admin", "password": "password123"})
    assert auth.status == 200
    token = auth.json()["token"]

    headers = {"Cookie": f"token={token}"}

    # 2️⃣ Create
    create = api.post(
        f"{BASE_URL}/booking",
        data=DATA_BOOK,
        headers=headers
        )
    assert create.status == 200
    print(create.json())
    assert_schema(create.json()["booking"], BOOKING_SCHEMA)
    assert_schema_pydantic(create.json()["booking"])
    booking_id = create.json()["bookingid"]
    print(f"{booking_id=}")
