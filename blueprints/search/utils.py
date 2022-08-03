from post import Post
from dao.posts_dao import PostsDAO


def search_for_posts(query: str) -> list[Post]:
    """Search all posts by a keyword"""
    posts_dao = PostsDAO()
    posts = posts_dao.load()
    result = []
    for post in posts:
        if query.lower() in post.content.lower():
            result.append(post)
            if len(result) == 10:
                # Отдавать только первые 10 результатов
                break
    return result
