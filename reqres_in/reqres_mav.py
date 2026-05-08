'''📌 Задание 08 (Reqres — Список пользователей)
Ресурс: https://reqres.in/api/users?page=2

Задача:

Отправьте GET-запрос для получения второй страницы списка пользователей
Выведите в консоль:
Page: 2
Total Pages: <значение поля total_pages>
First User on Page: <имя первого пользователя в массиве data>


Проверьте, что в ответе ровно 6 пользователей (поле data)

URL = "https://reqres.in/api/users?page=2"

response = requests.get(URL)'''


from playwright.sync_api import sync_playwright

BASE_URL = "https://reqres.in/api"
EP_ = "/users"

with sync_playwright() as drv:
    browser = drv.chromium.launch(headless=True)
    context = browser.new_context()
    api_ = context.request
    # resp = api_.get(BASE_URL + EP_)
    resp = api_.options(BASE_URL + EP_)
    print(resp.status)
    print(resp.json())
    # print("\n".join([str(item) for item in resp.json()]))
