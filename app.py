import logging
from dotenv import load_dotenv

from utils import create_app

from api.views import api
from bookmarks.views import bookmarks
from error.views import error_handlers
from main.views import main
from search.views import search

from config.constants import ACCESS_LOG_PATH

# Load environment variables from .env
load_dotenv()

logging.basicConfig(filename=ACCESS_LOG_PATH, level=logging.INFO)

app = create_app([api, bookmarks, error_handlers, main, search])

if __name__ == '__main__':
    app.run()
