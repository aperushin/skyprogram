from dao.bookmarks_dao import BookmarksDAO
from dao.posts_dao import PostsDAO
from flask import Blueprint, render_template

# Create blueprint
main = Blueprint('main', __name__, template_folder='templates')

# Create data access objects for posts and bookmarks
posts_dao = PostsDAO()
bookmarks_dao = BookmarksDAO()


@main.get('/')
def page_home():
    posts = posts_dao.load()

    bookmarks_list = bookmarks_dao.load()
    bookmarks_count = bookmarks_dao.get_count()

    return render_template(
        'index.html',
        posts=posts,
        bookmarks=bookmarks_list,
        bookmarks_count=bookmarks_count
    )


@main.get('/posts/<int:post_id>')
def page_post(post_id):
    post = posts_dao.get_by_id(post_id)
    return render_template('post.html', post=post)


@main.get('/users/<user_name>')
def page_user(user_name):
    posts = posts_dao.get_by_user(user_name)
    return render_template('user-feed.html', posts=posts)
