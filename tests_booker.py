from api.booker_api import BookerApi
from data.booking_url_api import BASE_URL, BOOKING
from data.booking_data_api import BOOKING_DATA


class TestsBooker:

    def test_booking_01(self, booker):
        resp = booker.get(f"{BOOKING}/1")
        print(f"{resp=}")
        assert 'firstname' in resp and 'lastname' in resp, \
            "Ответ не содержит имени и фамилии"

    # def test_booking_02(self):
    #     booker = BookerApi(BASE_URL)
    #     booker.login()
    #     print(f"\n{booker.auth_token=}")
    #     new_booking_id = booker.create_booking(BOOKING_DATA)
    #     print(f"{new_booking_id=}")
    #     booker.close()

    def test_booking_02(self, booker):
        resp = booker.get(f"{BOOKING}/1")
        print(f"{resp=}")
        assert 'firstname' in resp and 'lastname' in resp, \
            "Ответ не содержит имени и фамилии"

    def test_booking_03(self, booker):
        resp = booker.get(f"{BOOKING}/1")
        print(f"{resp=}")
        assert 'firstname' in resp and 'lastname' in resp, \
            "Ответ не содержит имени и фамилии"

    def test_booking_04(self, booker):
        resp = booker.get(f"{BOOKING}/1")
        print(f"{resp=}")
        assert 'firstname' in resp and 'lastname' in resp, \
            "Ответ не содержит имени и фамилии"
