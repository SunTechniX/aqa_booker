# src/webapp.py
import requests

def get_post_title(post_id: int) -> str:
    """ Получает заголовок поста из JSONPlaceholder """
    resp = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
        )
    resp.raise_for_status()
    return resp.json()["title"]


def send_notification(user_id: str, message: str) -> None:
    """Отправляет уведомление через внешний API"""
    requests.post(
        "https://api.example.com/notifications",
        json={"user_id": user_id, "message": message}
        )
