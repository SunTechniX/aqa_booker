import requests
from faker import Faker

URL = "https://reqres.in/api/users"
headers_ = {"x-api-key": "pub_4124d968b81b82ab2a9bc60e4c45c879b79e722b705d595aa37714bf87d9502c"}
data_json = {"name": "New Student", "job": "API Tester"}

fake = Faker()


def create_user():
    data_json = {
        "name": fake.name(),
        "job": "QA Engineer"
    }

    response = requests.post(
        url=URL,
        json=data_json,
        headers=headers_
    )

    json_response = response.json()
    user_id = json_response["id"]

    return user_id


def delete_user(user_id):
    response = requests.delete(
        url=f"{URL}/{user_id}", headers=headers_)

    return response.status_code


def get_user(user_id):
    response = requests.get(
        url=f"{URL}/{user_id}",
        headers=headers_
    )

    return response.status_code


def test_create_delete_user():
    user_id = create_user()
    print(f"[CREATE] ID: {user_id}")

    status_code_delete = delete_user(user_id)
    print(f"[DELETE] Status: {status_code_delete}")

    status_code_verify = get_user(user_id)
    print(f"[VERIFY] Status: {status_code_verify}")

    assert status_code_delete == 204
    assert status_code_verify == 404