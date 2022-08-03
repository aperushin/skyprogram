import pytest
from app import app as flask_app


@pytest.fixture
def post_data_keys():
    return {
        'poster_name', 'poster_avatar', 'pic', 'content',
        'views_count', 'likes_count', 'pk'
    }


def test_single_post_format():
    """Check if a request to a single post URL returns correct data type"""
    response = flask_app.test_client().get('/api/posts/2')
    assert isinstance(response.json, dict)


def test_single_post_keys(post_data_keys):
    """Check if a request to a single post URL returns data with correct keys"""
    response = flask_app.test_client().get('/api/posts/2')
    test_post = response.json
    test_keys = set(test_post.keys())
    assert test_keys.issuperset(post_data_keys)


def test_posts_format():
    """Check if a request to the URL for all posts returns correct data type"""
    response = flask_app.test_client().get('/api/posts')
    assert isinstance(response.json, list)


def test_posts_keys(post_data_keys):
    """Check if a request to the URL for all posts returns data with correct keys"""
    response = flask_app.test_client().get('/api/posts')
    test_post = response.json[0]
    test_keys = set(test_post.keys())
    assert test_keys.issuperset(post_data_keys)
