import requests

def get_post_title(post_id: int) -> str:
    """ Получает заголовок поста из JSONPlaceholder """
    resp = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
        )
    resp.raise_for_status()
    return resp.json()["title"]

def test_get_title(mocker):  # ← mocker — фикстура, как page или tmp_path
    # Патчим ВНУТРИ — сигнатура не меняется
    mock_get = mocker.patch("mocks.test_pytest_moker.requests.get")

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
