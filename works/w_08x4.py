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
        url=f"{URL}/{user_id}",
        headers=headers_
    )

    return response.status_code


def get_user(user_id):
    response = requests.get(
        url=f"{URL}/{user_id}",
        headers=headers_
    )

    return response.status_code

def get_users_in_page(numb):
    response_5 = requests.get(f"{URL}?page={numb}", headers=headers_)
    response_data = response_5.json()
    return response_data

def test_create_delete_user():
    user_id = create_user()
    print(f"[CREATE] ID: {user_id}")

    status_code_delete = delete_user(user_id)
    print(f"[DELETE] Status: {status_code_delete}")

    status_code_verify = get_user(user_id)
    print(f"[VERIFY] Status: {status_code_verify}")

    assert status_code_delete == 204
    assert status_code_verify == 404

def test_pagination():
    required_fields = ["page", "per_page", "total", "total_pages", "data"]

    for i in range(1,3):
        data_page_2 = get_users_in_page(i)
        for field in required_fields:
            assert field in data_page_2, f"Поле {field} отсутствует"
        per_page = data_page_2["per_page"]
        data_len = len(data_page_2["data"])
        assert data_len <= per_page

        print(f'[PAGE 1] Users: {data_len}, per_page: {per_page}')
