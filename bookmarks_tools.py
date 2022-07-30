from config import BOOKMARKS_FILE
from file_utils import load_json, write_json
from utils import get_posts_all


def get_bookmarks():
    return load_json(BOOKMARKS_FILE)


def get_posts_from_bookmarks():
    all_posts = get_posts_all()
    bookmarks = get_bookmarks()
    result = []
    for post in all_posts:
        if post.pk in bookmarks:
            result.append(post)
    return result


def add_post_to_bookmarks(post_id: int) -> None:
    bookmarks = get_bookmarks()
    if post_id not in bookmarks:
        bookmarks.append(post_id)
        write_json(bookmarks, BOOKMARKS_FILE)


def delete_post_from_bookmarks(post_id: int) -> None:
    bookmarks = get_bookmarks()
    if post_id in bookmarks:
        bookmarks.remove(post_id)
        write_json(bookmarks, BOOKMARKS_FILE)
