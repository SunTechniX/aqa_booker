import pytest

from sand_box.book_api import BookApi


@pytest.fixture
def book():
    book_ = BookApi()
    print("\nСоздали сессию")
    yield book_
    print("\nЗакрыли сессию")
    book_.close()
