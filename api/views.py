from flask import Blueprint, jsonify

from utils import get_logger
from config.constants import API_LOG_PATH
from posts_dao import PostsDAO

api = Blueprint('api', __name__)

# Create logger that writes to the specified file
api_logger = get_logger('api', filename=API_LOG_PATH)

# Create data access object for posts
posts_dao = PostsDAO()


@api.get('/api/posts')
def api_posts():
    posts = posts_dao.load()
    api_logger.info('GET /api/posts')
    return jsonify(posts)


@api.get('/api/posts/<int:post_id>')
def api_post_by_id(post_id):
    post = posts_dao.get_by_id(post_id)
    api_logger.info(f'GET /api/posts/{post_id}')
    return jsonify(post)
