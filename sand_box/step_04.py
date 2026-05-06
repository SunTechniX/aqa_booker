from playwright.sync_api import sync_playwright

from data.booking_url_api import BASE_URL, BOOKING

with sync_playwright() as drv:
    browser = drv.chromium.launch(headless=True)
    context = browser.new_context()
    api_ = context.request
    resp = api_.get(BASE_URL + BOOKING)
    print(resp.status)
    print("\n".join([str(item) for item in resp.json()]))
