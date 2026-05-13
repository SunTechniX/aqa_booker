# test_unittest_decorator.py
from unittest.mock import patch, Mock
from src.webapp import get_post_title


@patch("src.webapp.requests.get")  # ← Патчим ДО определения функции
def test_get_title(mock_get):  # ← mock_get приходит ПЕРВЫМ аргументом
    # Настраиваем мок
    mock_resp = Mock()
    mock_resp.json.return_value = {"title": "Mocked Title", "id": 1}
    mock_resp.raise_for_status = Mock()
    mock_get.return_value = mock_resp

    # Тестируем
    result = get_post_title(1)
    assert result == "Mocked Title"

    # Проверяем вызов
    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5
    )