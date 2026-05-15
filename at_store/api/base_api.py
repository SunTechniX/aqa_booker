from playwright.sync_api import APIRequestContext

from at_store.data.data_at_store import BASE_URL


class ApiBase:

    def __init__(self, drv_):
        # self.base_url = BASE_URL
        self.drv = drv_
        self.session: APIRequestContext = self.drv.request.new_context(
            base_url=BASE_URL,
            # extra_http_headers={
            #     # "Content-Type": "application/json"
            #     "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryVdhYCziHEBjvvvZg"
            #     }
            )
        self.auth_token = None

    def _check_status_code(self, code: int, expected_status_code: int = 200):
        assert code == expected_status_code, \
            f"Ожидали код {expected_status_code}, получили {code}"

    def get(self, endpoint: str, expected_status_code: int = 200):
        response = self.session.get(url=endpoint) #, headers=headers_)
        self._check_status_code(response.status, expected_status_code)

    def post(self, endpoint: str, data_json: dict = None,
             expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        try:
            # headers_ = {"Content-Type": "application/x-www-form-urlencoded"}
            response = self.session.post(url=endpoint, data=data_json)  # , headers=headers_)
        except ConnectionError as e:
            print("\n=== No Connection ===")
            raise AssertionError(e)
        self._check_status_code(response.status,
                                expected_status_code)

    def post_form(self, endpoint: str, data_json: dict = None,
                  expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        try:
            # headers_ = {"Content-Type": "application/x-www-form-urlencoded"} - само вставится при использовании form=
            response = self.session.post(url=endpoint, form=data_json)  # , headers=headers_)
        except ConnectionError as e:
            print("\n=== No Connection ===")
            raise AssertionError(e)
        self._check_status_code(response.status,
                                expected_status_code)

    def close(self):
        pass


class ApiBaseCtx:

    def __init__(self, ctx_):
        self.ctx = ctx_
        self.session: APIRequestContext = self.ctx.request
        self.auth_token = None

    def _check_status_code(self, code: int, expected_status_code: int = 200):
        assert code == expected_status_code, \
            f"Ожидали код {expected_status_code}, получили {code}"

    def get(self, endpoint: str, expected_status_code: int = 200):
        response = self.session.get(url=endpoint) #, headers=headers_)
        self._check_status_code(response.status, expected_status_code)

    def post(self, endpoint: str, data_json: dict = None,
             expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        try:
            # headers_ = {"Content-Type": "application/x-www-form-urlencoded"}
            response = self.session.post(url=endpoint, data=data_json)  # , headers=headers_)
        except ConnectionError as e:
            print("\n=== No Connection ===")
            raise AssertionError(e)
        self._check_status_code(response.status,
                                expected_status_code)

    def post_form(self, endpoint: str, data_json: dict = None,
                  expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        # headers_ = {"Content-Type": "application/x-www-form-urlencoded"} - само вставится при использовании form=
        response = self.session.post(url=endpoint, form=data_json)  # , headers=headers_)
        self._check_status_code(response.status,
                                expected_status_code)

    def post_form2(self, endpoint: str, data_json: dict = None,
                   expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        headers_ = {"Content-Type": "application/x-www-form-urlencoded"}
        response = self.session.post(url=endpoint, data=data_json, headers=headers_)
        self._check_status_code(response.status,
                                expected_status_code)

    def close(self):
        pass

