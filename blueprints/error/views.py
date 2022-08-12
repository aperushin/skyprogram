from flask import Blueprint

# Create blueprint
error_handlers = Blueprint('error_handlers', __name__)


@error_handlers.app_errorhandler(404)
def page_not_found(e):
    return '<h1>Страница не найдена</h1>', 404


@error_handlers.app_errorhandler(500)
def internal_server_error(e):
    return '<h1>Что-то пошло не так…</h1>', 500
