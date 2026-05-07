import requests


class BasePetApi:

    def __init__(self, base_url):
        self.base_url = base_url

    def _check_status_code(self, code: int, expected_status_code: int = 200):
        assert code == expected_status_code, \
            f"Ожидали код {expected_status_code}, получили {code}"

    def get(self, endpoint: str,
                 expected_status_code: int = 200):
        response = requests.get(url=f"{self.base_url}{endpoint}")
        self._check_status_code(response.status_code, expected_status_code)
        return response.json()

    def post(self, endpoint: str, data_json: dict = None,
             expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        response = requests.post(url=f"{self.base_url}{endpoint}",
                                 json=data_json)
        self._check_status_code(response.status_code, expected_status_code)
        return response.json()

    def put(self, endpoint: str, data_json: dict = None,
            expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        response = requests.put(url=f"{self.base_url}{endpoint}",
                                json=data_json)
        self._check_status_code(response.status_code, expected_status_code)
        return response.json()

    def delete(self):
        pass
