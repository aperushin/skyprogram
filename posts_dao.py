from config.constants import DATA_FILE
from file_utils import load_json
from post import Post


class PostsDAO:

    @staticmethod
    def load() -> list[Post]:
        """Load all posts from the file, initializing Post class instances"""
        posts_data = load_json(DATA_FILE)
        posts = [Post(**post) for post in posts_data]
        return posts

    def get_by_id(self, post_id: int) -> Post:
        """Get a single post by its id"""
        posts = self.load()

        for post in posts:
            if post.pk == post_id:
                return post

    def get_by_user(self, user_name: str) -> list[Post]:
        """Get a list of posts by poster's username"""
        posts = self.load()
        result = []

        for post in posts:
            if post.poster_name == user_name:
                result.append(post)
        return result
