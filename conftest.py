import pytest

from api.booker_api import BookerApi
from data.booking_url_api import BASE_URL


#@pytest.fixture(scope="session")

@pytest.fixture
def booker(worker_id):
    booker = BookerApi(BASE_URL)
    if "gw" in worker_id:
        user_ = f"BOOKER_NAME_{worker_id.upper()}"
        pass_ = f"BOOKER_PASSWORD_{worker_id.upper()}"
    else:
        user_ = "BOOKER_NAME_GW0"
        pass_ = "BOOKER_PASSWORD_GW0"
    f = open(f"gw/work_{worker_id}.txt", "w")
    f.write(f"{user_}\n{pass_}")
    f.close()
    booker.login(user_, pass_)
    yield booker
    booker.close()

@pytest.fixture
def booker_():
    booker = BookerApi(BASE_URL)
    booker.login()
    yield booker
    booker.close()
