from at_store.api.store_api import ApiStore
from at_store.data.data_at_store import DATA_REGISTER_LOGIN, DATA_LOGIN
from at_store.helpers.utils import load_data
from at_store.page.login_create_page import LoginCreatePage
from at_store.page.login_page import LoginPage
from at_store.page.main_page import MainPage


class TestAT:

    @staticmethod
    def interceptor(route):
        if route.request.resource_type not in ("font", "image", "script",
                                               "stylesheet", "other"):
            print(f"🔍 {route.request.method} {route.request.url} [{route.request.resource_type}]")
            if route.request.resource_type == "document":
                if hasattr(route.request, "body") and route.request.body:
                    print(route.request.body[:50])
                if hasattr(route.request, "data") and route.request.data:
                    print(route.request.data[:50])
                if hasattr(route.request, "form") and route.request.form:
                    print(route.request.form[:50])
                if "create" in route.request.url:
                    print(route.request.__dict__)
        route.continue_()

    def test_at_login_01(self, context, page):  # driver

        at = MainPage(page)
        print()
        at.page.route("**/*", self.interceptor)
        at.open()
        at.click_login()

        # Страница Login
        at_login = LoginPage(page)
        # Нажали Continue
        at_login.click_btn_continue()

        data_for_register_form = DATA_REGISTER_LOGIN.copy()
        data_for_login_form = DATA_LOGIN.copy()

        api = ApiStore(context)  # ApiStore(driver)
        tokens = at_login.csrftoken_create
        instance = at_login.csrfinstance_create
        load_data(data_for_register_form, tokens, instance)
        api.create_user(data_for_register_form)  # API Create

        at.page.wait_for_timeout(15_000)
        at.open()

        at.click_login()
        at_login.fill_login_form(data_for_login_form)
        at_login.click_btn_login()
        at.page.wait_for_timeout(15_000)

        # at.click_login()
        # at_reg.click_btn_login()
        #
        # # Отправить API-Login
        # api.login_open()
        #
        # tokens = at_reg.csrftoken_login
        # instance = at_reg.csrfinstance_login
        # load_data(data_for_login_form, tokens, instance)
        # api.login_user(data_for_register_form)
        #
        # at_reg.page.wait_for_timeout(2_000)
        # api.check_user()
        at.open()
        at.page.reload()
        at.page.wait_for_timeout(5_000)

    def test_at_login_02(self, context, page):  # driver
        # 1. Главная
        at = MainPage(page)
        print()
        at.page.route("**/*", self.interceptor)
        at.open()
        at.click_login()

        # 2. Страница Login
        at_login = LoginPage(page)
        # Нажали Continue
        at_login.click_btn_continue()

        # данные
        data_for_register_form = DATA_REGISTER_LOGIN.copy()
        data_for_login_form = DATA_LOGIN.copy()

        # 3. Страница формы создания Login-а
        at_create = LoginCreatePage(page)
        at_create.fill_login_create_form(data_for_register_form)
        at_create.click_btn_continue()


        at_login.page.wait_for_timeout(2_000)
        at_login.page.pause()
        at.open()
        at.page.reload()

        # at.click_login()
        # at_login.fill_login_form(data_for_login_form)
        # at_login.click_btn_login()

        at.page.wait_for_timeout(5_000)
