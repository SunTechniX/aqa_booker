# test_pytest_mocker.py
import pytest
import requests
from src.webapp import get_post_title, send_notification

def test_get_title(mocker):  # ← mocker — фикстура, как page или tmp_path
    # Патчим ВНУТРИ — сигнатура не меняется
    mock_get = mocker.patch("src.webapp.requests.get")

    # Настраиваем (синтаксис идентичен unittest.mock!)
    mock_resp = mocker.Mock()
    mock_resp.json.return_value = {"title": "Mocked Title", "id": 1}
    mock_resp.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_resp

    # Тестируем
    result = get_post_title(1)
    assert result == "Mocked Title"

    # Проверяем (методы те же!)
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5
        )

def test_api_error(mocker):
    mock_get = mocker.patch("src.webapp.requests.get")
    
    # Имитируем ошибку сети
    mock_get.side_effect = requests.Timeout("Connection timeout")
    
    with pytest.raises(requests.Timeout):
        get_post_title(1)

def test_multiple_calls(mocker):
    mock_get = mocker.patch("src.webapp.requests.get")

    # ✅ Моки настроены верно
    mock_get.side_effect = [
        mocker.Mock(
            json=mocker.Mock(return_value={"title": "First", "id": 1})),
        mocker.Mock(
            json=mocker.Mock(return_value={"title": "Second", "id": 2})),
        requests.HTTPError("Not Found"),
        ]

    # ✅ Функция уже возвращает строку, повторный ["title"] не нужен
    assert get_post_title(1) == "First"
    assert get_post_title(2) == "Second"
    with pytest.raises(requests.HTTPError):
        get_post_title(3)


def test_call_verification(mocker):
    # Патчим requests.post ТАМ, ГДЕ ОН ИСПОЛЬЗУЕТСЯ
    mock_post = mocker.patch("src.webapp.requests.post")

    # Вызываем нашу функцию дважды
    send_notification("user123", "Welcome!")
    send_notification("user456", "Hello!")

    # 1. Последний вызов должен быть таким:
    mock_post.assert_called_with(
        "https://api.example.com/notifications",
        json={"user_id": "user456", "message": "Hello!"}
    )

    # 2. Хотя бы один вызов с такими аргументами:
    mock_post.assert_any_call(
        "https://api.example.com/notifications",
        json={"user_id": "user123", "message": "Welcome!"}
    )

    # 3. Все вызовы в строгом порядке:
    mock_post.assert_has_calls([
        mocker.call("https://api.example.com/notifications",
                    json={"user_id": "user123", "message": "Welcome!"}),
        mocker.call("https://api.example.com/notifications",
                    json={"user_id": "user456", "message": "Hello!"}),
    ])

    # 4. Общее количество вызовов:
    assert mock_post.call_count == 2
