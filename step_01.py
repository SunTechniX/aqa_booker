from api.api_client import ApiClient
from data.api_url import BASE_URL
from data.api_user_data import BOOKING_DATA

api_client = ApiClient(BASE_URL)
api_client.login()
create_booking = api_client.create_booking(BOOKING_DATA)
print(f"{create_booking=}")
api_client.close()

# https://restful-booker.herokuapp.com/booking"
# response = requests.get(f"{BASE_URL}{BOOKING}/1")
# response_data = parse_response(response)
# print(f"Body: {response_data}")
# assert 'firstname' in response_data and 'lastname' in response_data, \
#     "Ответ не содержит имени и фамилии"
