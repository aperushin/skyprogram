import pytest
from post import Post


class TestPost:

    standard_post_data = {
        'poster_name': 'johnny',
        'poster_avatar': 'https://example.com/pic.jpg',
        'pic': 'https://example.com/pic.jpg',
        'content': 'Sample text, sample text. #Sample #text',
        'views_count': 100,
        'likes_count': 101,
        'pk': 1
    }

    def test_content_short_short(self):
        post_data = self.standard_post_data
        post = Post(**post_data)
        # Post content shorter than 50 symbols should be left unchanged
        assert post.content_short == post_data['content']

    def test_content_short_long(self):
        # Using dict() to make a new copy of data from the field
        post_data = dict(self.standard_post_data)

        # 51 symbol
        post_data['content'] = 'Sample text, sample text. Sample text #Sample #text'

        post = Post(**post_data)
        assert post.content_short == 'Sample text, sample text. Sample text #Sample #tex …'

    def test_content_tagged(self):
        post_data = self.standard_post_data
        post = Post(**post_data)
        assert post.content_tagged == (
            '''Sample text, sample text. <a href="/tag/sample">#Sample</a> <a href="/tag/text">#text</a>'''
        )
