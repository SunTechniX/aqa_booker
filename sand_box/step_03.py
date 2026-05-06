from data.booking_data_api import BOOKING_DATA
from data.booking_url_api import BOOKING


def test_step_03(book):  # -= 4 =-
    print(book.get_booking_all)
    print("-------------------------")
    resp_json = book.set_booking(BOOKING_DATA)
    print(resp_json)
    print("-------------------------")
    resp_json = book.get_booking_by_id(resp_json["bookingid"])
    print(resp_json)
