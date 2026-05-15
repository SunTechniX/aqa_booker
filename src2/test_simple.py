import requests
from unittest.mock import patch, Mock
from webapp import get_post_title


def test_simple():
    get_post_title(2)


def test_mock_01():
    # Создаём мок вручную
    my_mock = Mock()
    my_mock.json.return_value = {"title": "Manual Mock", "id": 1}
    my_mock.raise_for_status = Mock()

    # Патчим и сразу возвращаем наш мок
    with patch("src2.webapp.requests.get", return_value=my_mock):
        result = get_post_title(2)
        assert result == "Manual Mock"

def test_mock_02():
    with patch.object(requests, "get") as mock_get:
        my_mock = Mock()
        my_mock.json.return_value = {"title": "Manual Mock", "id": 1}
        my_mock.raise_for_status = Mock()
        mock_get.return_value = my_mock

        result = get_post_title(2)
        assert result == "Manual Mock"

def test_mock_03():
    with patch("src2.webapp.requests.get") as mock_get:
        my_mock = Mock()
        my_mock.json.return_value = {"title": "Manual Mock", "id": 1}
        my_mock.raise_for_status = Mock()
        mock_get.return_value = my_mock

        result = get_post_title(2)
        assert result == "Manual Mock"

@patch("src2.webapp.requests.get")
def test_mock_04(mock_get):
    my_mock = Mock()
    my_mock.json.return_value = {"title": "Manual Mock", "id": 1}
    my_mock.raise_for_status = Mock()
    mock_get.return_value = my_mock

    result = get_post_title(2)
    assert result == "Manual Mock"


def test_mock_05(mocker):
    mock_get = mocker.patch("src2.webapp.requests.get")

    my_mock = mocker.Mock()
    my_mock.json.return_value = {"title": "Manual Mock", "id": 1}
    my_mock.raise_for_status = mocker.Mock()
    mock_get.return_value = my_mock

    result = get_post_title(2)
    assert result == "Manual Mock"
