import pytest
from posts_dao import PostsDAO
from post import Post


@pytest.fixture
def posts():
    posts_data = [
        {
            'poster_name': 'johnny',
            'poster_avatar': 'https://example.com/pic.jpg',
            'pic': 'https://example.com/pic.jpg',
            'content': 'Sample text, sample text. #Sample #text',
            'views_count': 100,
            'likes_count': 101,
            'pk': 1
        },
        {
            'poster_name': 'bob',
            'poster_avatar': 'https://example.com/pic.jpg',
            'pic': 'https://example.com/pic.jpg',
            'content': 'Sample text, sample text. #Sample #text',
            'views_count': 50,
            'likes_count': 20,
            'pk': 2
        }
    ]
    return [Post(**p) for p in posts_data]


def test_get_by_id(posts, monkeypatch):
    monkeypatch.setattr(PostsDAO, 'load', lambda _: posts)
    posts_dao = PostsDAO()
    test_post = posts_dao.get_by_id(2)
    assert test_post == posts[1]


def test_get_by_user(posts, monkeypatch):
    monkeypatch.setattr(PostsDAO, 'load', lambda _: posts)
    posts_dao = PostsDAO()
    test_post = posts_dao.get_by_user('bob')
    assert test_post == [posts[1]]
