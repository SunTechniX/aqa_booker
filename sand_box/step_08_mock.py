# src/webapp.py
import requests

def get_post_title(post_id: int) -> str:
    """Получает заголовок поста из JSONPlaceholder"""
    resp = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
    )
    resp.raise_for_status()
    return resp.json()["title"]  # JSONPlaceholder точно возвращает {"title": "..."}

# test_webapp_bad.py
# from src.webapp import get_post_title

def test_get_title_real():
    # ❌ Реальный запрос в интернет — медленно, нестабильно, зависит от сети
    result = get_post_title(1)
    print(result)
    assert result == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    # ⚠️ Тест может упасть, если API недоступен, или если данные изменятся


# test_webapp_good.py
import pytest
from unittest.mock import patch, Mock
# from src.webapp import get_post_title


def test_get_title_mocked():
    # ✅ Мокаем requests.get, чтобы не делать реальный запрос
    mock_response = Mock()
    mock_response.json.return_value = {"title": "Mocked Title", "id": 1,
                                       "userId": 1, "body": "..."}
    mock_response.raise_for_status = Mock()  # ничего не делает, но метод есть

    # with patch("src.webapp.requests.get", return_value=mock_response):
    with patch("sand_box.step_08_mock.requests.get", return_value=mock_response):
        result = get_post_title(1)
        print(result)

    assert result == "Mocked Title"
    # ✅ Тест быстрый, стабильный, не зависит от сети
