import pytest
from dao.bookmarks_dao import BookmarksDAO


class TestBookmarksDAO:

    @pytest.fixture
    def bookmarks_test_data(self):
        return [1, 2, 5]

    @pytest.fixture
    def bookmarks_dao(self):
        return BookmarksDAO()

    def test_load(self, bookmarks_dao):
        """Check if loaded bookmarks are of the correct data type"""
        bookmarks = bookmarks_dao.load()
        assert isinstance(bookmarks, list)

    def test_count(self, monkeypatch, bookmarks_test_data, bookmarks_dao):
        """oh boy"""
        monkeypatch.setattr(BookmarksDAO, 'load', lambda _: bookmarks_test_data)
        bookmarks_count = bookmarks_dao.get_count()
        assert bookmarks_count == 3

# TODO: add more tests
