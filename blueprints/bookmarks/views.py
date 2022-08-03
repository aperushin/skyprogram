from flask import Blueprint, redirect, render_template

from dao.bookmarks_dao import BookmarksDAO

# Create blueprint
bookmarks = Blueprint('bookmarks', __name__, template_folder='templates')

# Create data access object for bookmarks
bookmarks_dao = BookmarksDAO()


@bookmarks.get('/bookmarks')
def page_bookmarks():
    posts = bookmarks_dao.get_posts()
    return render_template('bookmarks.html', posts=posts)


@bookmarks.get('/bookmarks/add/<int:post_id>')
def add_bookmark(post_id):
    bookmarks_dao.add(post_id)
    return redirect('/', code=302)


@bookmarks.get('/bookmarks/remove/<int:post_id>')
def remove_bookmark(post_id):
    bookmarks_dao.delete(post_id)
    return redirect('/', code=302)
