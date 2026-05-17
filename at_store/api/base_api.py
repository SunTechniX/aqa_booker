import time
from playwright.sync_api import APIRequestContext

from at_store.data.data_at_store import BASE_URL
from at_store.tests.test_register_fixed import extract_visible_errors


class ApiBaseCtx:

    def __init__(self, ctx_):
        self.ctx = ctx_
        self.session: APIRequestContext = self.ctx.request
        self.auth_token = None
        self.response = None
        self.timestamp = int(time.time())

    def _check_status_code(self, expected_status_code: int = 200):
        assert self.response.status == expected_status_code, \
            f"Ожидали код {expected_status_code}, получили {self.response.status}"

    def get(self, endpoint: str, expected_status_code: int = 200):
        self.response = self.session.get(url=endpoint) #, headers=headers_)
        self._check_status_code(expected_status_code)
        return self.response

    def post(self, endpoint: str, data_json: dict = None,
             expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        try:
            # headers_ = {"Content-Type": "application/x-www-form-urlencoded"}
            self.response = self.session.post(url=endpoint, data=data_json)  # , headers=headers_)
        except ConnectionError as e:
            print("\n=== No Connection ===")
            raise AssertionError(e)
        self._check_status_code(expected_status_code)

    def post_form(self, endpoint: str, data_json: dict = None,
                  expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        # headers_ = {"Content-Type": "application/x-www-form-urlencoded"} - само вставится при использовании form=
        self.response = self.session.post(url=endpoint, form=data_json)  # , headers=headers_)
        self._check_status_code(expected_status_code)
        return self.response

    def post_form2(self, endpoint: str, data_json: dict = None,
                   expected_status_code: int = 200):
        assert data_json is not None, "Тело не заполнено!"
        print(f"\n{data_json=}")
        headers_ = {"Content-Type": "application/x-www-form-urlencoded"}
        self.response = self.session.post(url=endpoint, data=data_json, headers=headers_)
        self._check_status_code(expected_status_code)
        return self.response

    def close(self):
        pass

    def check_html_for_errors(self):
        """ Ищем ошибки на Web-странице """
        errors = extract_visible_errors(self.response.text())
        if errors:
            print(f"Ошибки сервера:")
            for e in errors:
                print(f"   • {e}")
            with open(f"error_on_web_{self.timestamp}.html", "w", encoding="utf-8") as f:
                f.write(self.response.text())
            assert False, f"Registration failed: {errors[0]}"

    def check_reg_form(self):
        """ Если вернулась форма — возможно, тихая ошибка """
        if "AccountFrm" in self.response.text():
            print("⚠️  Вернулась форма регистрации — сохраняем для анализа")
            with open(f"error_on_reg_form_{self.timestamp}.html", "w",
                      encoding="utf-8") as f:
                f.write(self.response.text())
