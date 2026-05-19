class AnyClass:

    def __init__(self, status = 222):
        self.status_code = status

    def json(self):
        return {"Trali": "Vally"}


def any_fun():
    return AnyClass()


def any_mock(mocker_):  # ← mocker — фикстура, как page или tmp_path
    # Патчим ВНУТРИ — сигнатура не меняется
    mock_get = mocker_.patch("mocks.mock_00.any_fun")

    mock_resp = mocker_.Mock()
    mock_resp.json.return_value = {"user_id": 123, "email": "test@example.com"}
    mock_resp.status_code = 201
    mock_resp.raise_for_status = mocker_.Mock()
    mock_get.return_value = mock_resp


def test_mock_00(mocker):
    any_mock(mocker)
    rez = any_fun()
    print()
    print(rez.status_code)
    print(rez.json())