import logging
from config import DATA_FILE
from post import Post
from file_utils import load_json


def get_logger(name: str, filename: str) -> logging.Logger:
    """Get or create a logger with a file handler"""
    logger = logging.getLogger(name)
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    file_handler = logging.FileHandler(filename, encoding='utf8')
    file_handler.setFormatter(log_formatter)

    logger.addHandler(file_handler)
    return logger


def get_posts_all() -> list[Post]:
    posts_data = load_json(DATA_FILE)
    posts = [Post(**post) for post in posts_data]
    return posts


def get_post_by_id(post_id: int) -> Post:
    posts = get_posts_all()
    for post in posts:
        if post.pk == post_id:
            return post


def get_posts_by_user(user_name: str) -> list[Post]:
    posts = get_posts_all()
    result = []
    for post in posts:
        if post.poster_name == user_name:
            result.append(post)
    return result


def search_for_posts(query: str) -> list[Post]:
    posts = get_posts_all()
    result = []
    for post in posts:
        if query.lower() in post.content.lower():
            result.append(post)
            if len(result) == 10:
                # Отдавать только первые 10 результатов
                break
    return result


def search_posts_by_tag(tagname):
    posts = get_posts_all()
    result = []
    for post in posts:
        if tagname.lower() in post.content_tagged.lower():
            result.append(post)
            if len(result) == 10:
                # Отдавать только первые 10 результатов
                break
    return result
