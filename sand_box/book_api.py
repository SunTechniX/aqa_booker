from data.booking_url_api import BOOKING
from sand_box.base_api import BaseApi


class BookApi(BaseApi):  # -= 3 =-

    def get_booking_all(self):
        return self.get(BOOKING)

    def get_booking_by_id(self, id):
        return self.get(BOOKING + f"/{id}")

    def set_booking(self, data):
        return self.post(BOOKING, data)
