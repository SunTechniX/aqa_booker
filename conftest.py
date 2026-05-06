import pytest

from api.booker_api import BookerApi
from data.booking_url_api import BASE_URL


#@pytest.fixture(scope="session")

@pytest.fixture
def booker():
    booker = BookerApi(BASE_URL)
    booker.login()
    yield booker
    booker.close()
