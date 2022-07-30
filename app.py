import logging

import bookmarks_tools
from flask import Flask, render_template, request, redirect, jsonify

import utils
from config import ACCESS_LOG_PATH, API_LOG_PATH

logging.basicConfig(filename=ACCESS_LOG_PATH, level=logging.INFO)

api_logger = utils.get_logger('api', filename=API_LOG_PATH)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.get('/')
def page_home():
    posts = utils.get_posts_all()
    bookmarks = bookmarks_tools.get_bookmarks()
    bookmarks_count = len(bookmarks)
    return render_template(
        'index.html',
        posts=posts,
        bookmarks=bookmarks,
        bookmarks_count=bookmarks_count
    )


@app.get('/posts/<int:postid>')
def page_post(postid):
    post = utils.get_post_by_id(postid)

    result = render_template(
        'post.html',
        post=post
    )
    return result


@app.get('/search/')
def page_search():
    query = request.args.get('s')
    if query:
        posts_found = utils.search_for_posts(query)
        results_count = len(posts_found)
        return render_template(
            'search.html',
            posts=posts_found,
            results_count=results_count,
            query=query
        )
    # If no arguments provided, return an empty search page
    return render_template('search.html')


@app.get('/users/<user_name>')
def page_user(user_name):
    posts = utils.get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=posts)


@app.get('/bookmarks')
def page_bookmarks():
    posts = bookmarks_tools.get_posts_from_bookmarks()
    return render_template('bookmarks.html', posts=posts)


@app.get('/tag/<tag_name>')
def page_tag(tag_name):
    hashtag = '#' + tag_name
    posts = utils.search_for_posts(hashtag)
    return render_template('tag.html', posts=posts, tag=tag_name)


@app.get('/bookmarks/add/<int:post_id>')
def add_bookmark(post_id):
    bookmarks_tools.add_post_to_bookmarks(post_id)
    return redirect('/', code=302)


@app.get('/bookmarks/remove/<int:post_id>')
def remove_bookmark(post_id):
    bookmarks_tools.delete_post_from_bookmarks(post_id)
    return redirect('/', code=302)


@app.get('/api/posts')
def api_posts():
    posts = utils.get_posts_all()
    api_logger.info('GET /api/posts')
    return jsonify(posts)


@app.get('/api/posts/<int:post_id>')
def api_post_by_id(post_id):
    post = utils.get_post_by_id(post_id)
    api_logger.info(f'GET /api/posts/{post_id}')
    return jsonify(post)


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Страница не найдена</h1>', 404


@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>Что-то пошло не так…</h1>', 500


if __name__ == '__main__':
    app.run()
