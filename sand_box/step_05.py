import pytest

from playwright.sync_api import sync_playwright, APIRequestContext

BASE_URL = "https://restful-booker.herokuapp.com"
DATA_BOOK = {"firstname": "Alex", "lastname": "Test", "totalprice": 150,
             "depositpaid": True,
             "bookingdates": {"checkin": "2026-05-01",
                              "checkout": "2026-05-05"},
             "additionalneeds": "WiFi"}


@pytest.fixture(scope="module")
def context():
    with sync_playwright() as drv:
        browser = drv.chromium.launch(headless=True)
        context_ = browser.new_context()
        yield context_
        context_.close()
        browser.close()

def test_full_workflow_via_context(context):
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
    booking_id = create.json()["bookingid"]

    # 3️⃣ Verify
    get = api.get(f"{BASE_URL}/booking/{booking_id}")
    assert get.status == 200
    assert get.json()["firstname"] == "Alex"

    # 4️⃣ Cleanup
    delete = api.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    assert delete.status == 201
