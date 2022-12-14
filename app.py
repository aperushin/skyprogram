import logging
from dotenv import load_dotenv

from utils import create_app
from config.constants import ACCESS_LOG_PATH

# Import blueprints
from blueprints.api.views import api
from blueprints.bookmarks.views import bookmarks
from blueprints.error.views import error_handlers
from blueprints.main.views import main
from blueprints.search.views import search

# Load environment variables from .env
load_dotenv(override=True)

# Specify the file to write the default Flask log to
logging.basicConfig(filename=ACCESS_LOG_PATH, level=logging.INFO)

# Create app registering the imported blueprints
app = create_app([api, bookmarks, error_handlers, main, search])

if __name__ == '__main__':
    app.run()
