from api.base_book_api import BaseBookApi
from data.booking_url_api import BOOKING


class BookerApi(BaseBookApi):

    def __init__(self, base_url: str):
        super().__init__(base_url)
        print(f"{self.session.headers=}")

    def create_booking(self, booking_data):
        response = self.post(endpoint=BOOKING, data_json=booking_data)
        return response["bookingid"]

    # def get_token(self):
    #     url = f"{self.base_url}{AUTH}"
    #     json_data = {"username": os.getenv("BOOKER_NAME"),
    #                  "password": os.getenv("BOOKER_PASSWORD")}
    #     response = requests.post(url, json=json_data,
    #                              headers=HEADERS_DATA)
    #     response_data = self.response_json_with_status(response)
    #     assert "token" in response_data, "Токен не получен"
    #     return response_data["token"]
