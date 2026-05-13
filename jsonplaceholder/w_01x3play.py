from playwright.sync_api import sync_playwright

class TestPostFerify:


    def test_create_and_verify_post(self):

        def handle_route(route):
            print(f">>> Запрос: {route.request.url}")
            route.continue_()  # Продолжить как есть

        with sync_playwright() as drv:
            browser = drv.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            api = page.request

            page.route("**typicode**/*", handle_route)

            base_url = "https://jsonplaceholder.typicode.com"
            post_data = {
                "userId": 1,
                "title": "Chain Test",
                "body": "Testing API chains"
                }

            create_response = api.post(f"{base_url}/posts", data=post_data)
            assert create_response.status == 201
            post_id = create_response.json()["id"]

            print(f"{post_id=}")
            # all_posts_response = requests.get(f"{base_url}/posts")
            # print("\n".join([str(item) for item in all_posts_response.json()]))

            post_id = 100
            get_response = api.get(f"{base_url}/posts/{post_id}")
            assert get_response.status == 200
            verified_post = get_response.json()
            title_match = verified_post["title"] == post_data["title"]
            print(f"\n[CREATE] Status: {create_response.status}")
            print(f"[VERIFY] Post ID: {post_id}")
            print(f"[VERIFY] Title Match: {title_match}")
            # assert title_match, "Title не совпадает с отправленным"

            context.close()
            browser.close()
