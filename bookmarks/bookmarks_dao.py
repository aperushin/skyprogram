from config.constants import BOOKMARKS_FILE
from file_utils import load_json, write_json
from post import Post
from posts_dao import PostsDAO


class BookmarksDAO:

    @staticmethod
    def load() -> list[int]:
        """Load bookmarks from file"""
        return load_json(BOOKMARKS_FILE)

    @staticmethod
    def write(data: list[int]) -> None:
        """Write bookmarks list to a file, overwriting the contents"""
        write_json(data, BOOKMARKS_FILE)

    def get_posts(self) -> list[Post]:
        """Get all bookmarked posts"""
        posts_dao = PostsDAO()
        all_posts: list[Post] = posts_dao.load()
        bookmarks = self.load()
        result = []

        for post in all_posts:
            if post.pk in bookmarks:
                result.append(post)

        return result

    def add(self, post_id: int) -> None:
        """Append post id to the bookmark list"""
        bookmarks = self.load()

        if post_id not in bookmarks:
            bookmarks.append(post_id)
            write_json(bookmarks, BOOKMARKS_FILE)

    def delete(self, post_id: int) -> None:
        """Remove post id from the bookmark list"""
        bookmarks: list = self.load()

        if post_id in bookmarks:
            bookmarks.remove(post_id)
            self.write(bookmarks)

    def get_count(self) -> int:
        """Get the count of bookmarks"""
        bookmarks = self.load()
        return len(bookmarks)
