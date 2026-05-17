from faker import Faker

fake = Faker()

BASE_URL = "https://www.automationteststore.com"
BASE_URL_NO_WWW = "https://www.automationteststore.com"

U_NAME = fake.user_name().replace(" ", "_")
#U_PASS = fake.password("")
U_NAME = "mama_i_papa"
U_PASS = "mama_papa"


DATA_REGISTER_LOGIN = {
    "csrftoken": "None",
    "csrfinstance": "0",
    "firstname": "mama",
    "lastname": "papa",
    "email": fake.email(),
    "telephone": "123456789",
    # "company": "Simbik",
    # "address_1": "Адрес",
    # "address_2": "",
    # "city": "Ульяновск",
    # "zone_id": "2795",
    # "postcode": "432054",
    # "country_id": "176",
    "loginname": U_NAME,
    "password": U_PASS,
    "confirm": U_PASS,
    # "newsletter": "0",
    "agree": "1",
    "account": "register"
    }

DATA_REGISTER = {
    "csrftoken": "None",
    "csrfinstance": "3",
    "account": "register"
    }

DATA_LOGIN = {
    "csrftoken": "None",
    "csrfinstance": "0",
    "loginname": U_NAME,
    "password": U_PASS,
    "account": "login"
    }
