import requests
import time

class TestPostFerify:

    def test_create_and_verify_post(self):
        base_url = "https://jsonplaceholder.typicode.com"
        post_data = {
            "userId": 1,
            "title": "Chain Test",
            "body": "Testing API chains"
        }
        create_response = requests.post(f"{base_url}/posts", json=post_data)
        assert create_response.status_code == 201
        post_id = create_response.json()["id"]
        print(f"{create_response.json()=}")
        # time.sleep(1)
        url = f"{base_url}/posts/{post_id}"
        print(url)
        get_response = requests.get(url)
        print(f"Error: {get_response.json()}")
        assert get_response.status_code == 200
        verified_post = get_response.json()
        title_match = verified_post["title"] == post_data["title"]
        print(f"\n[CREATE] Status: {create_response.status_code}")
        print(f"[VERIFY] Post ID: {post_id}")
        print(f"[VERIFY] Title Match: {title_match}")
        assert title_match, "Title не совпадает с отправленным"
