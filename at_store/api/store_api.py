from at_store.api.base_api import ApiBase, ApiBaseCtx
from at_store.api.urls import EP_BASE, EP_USER_CREATE, EP_USER_SUCCESS, \
    EP_USER_LOGIN
from at_store.data.data_at_store import BASE_URL


class ApiStore(ApiBaseCtx):

    def create_user(self, data_json: dict):
        """
        https://automationteststore.com/index.php?rt=account/create
        POST
        """
        endpoint = EP_BASE + EP_USER_CREATE
        # endpoint = BASE_URL + EP_BASE + EP_USER_CREATE
        print(f"🔍 POST-form Create: {endpoint=}")
        resp = self.post_form(endpoint, data_json=data_json,
                              expected_status_code=200)  # 302
        return resp

    def login_open(self):
        endpoint = EP_BASE + EP_USER_LOGIN
        print(f"🔍 GET Open: {endpoint=}")
        resp = self.get(endpoint, expected_status_code=200)
        return resp

    def login_user(self, data_json: dict):
        endpoint = EP_BASE + EP_USER_LOGIN
        print(f"🔍 POST-form Login: {endpoint=}")
        resp = self.post_form(endpoint, data_json=data_json,
                              expected_status_code=200)  # 302
        return resp

    def check_user(self):
        endpoint = EP_BASE + EP_USER_SUCCESS
        print(f"🔍 GET Check: {endpoint=}")
        resp = self.get(endpoint)
        return resp
