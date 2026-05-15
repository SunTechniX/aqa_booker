import requests

def get_post_title(post_id: int) -> str:
    """ Получает заголовок поста из JSONPlaceholder """
    resp = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
        )
    resp.raise_for_status()
    title_inside = resp.json()["title"]
    print(f"\n{title_inside=}")
    return title_inside