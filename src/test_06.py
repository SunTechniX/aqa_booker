import pytest
from src.webapp import get_post_title

@pytest.mark.parametrize("post_id,expected_title", [
    (1, "Post One"),
    (2, "Post Two"),
    (999, "Nonexistent Post"),
])
def test_get_title_parametrized(mocker, post_id, expected_title):
    # Мок создаётся ВНУТРИ — порядок аргументов не важен!
    mock_get = mocker.patch("src.webapp.requests.get")
    
    mock_resp = mocker.Mock()
    mock_resp.json.return_value = {"title": expected_title, "id": post_id}
    mock_resp.raise_for_status = mocker.Mock()
    mock_get.return_value = mock_resp
    
    result = get_post_title(post_id)
    assert result == expected_title
    
    mock_get.assert_called_once_with(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
        timeout=5
        )
