# test_unittest_context.py
from unittest.mock import patch, Mock
from src.webapp import get_post_title


def test_get_title():
    # Патчим ВНУТРИ функции — сигнатура не меняется
    with patch("src.webapp.requests.get") as mock_get:
        mock_resp = Mock()
        mock_resp.json.return_value = {"title": "Mocked Title", "id": 1}
        mock_resp.raise_for_status = Mock()
        mock_get.return_value = mock_resp

        result = get_post_title(1)
        assert result == "Mocked Title"
        mock_get.assert_called_once()
