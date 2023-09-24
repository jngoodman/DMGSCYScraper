from os import path, makedirs
from src.pull_html import HTML_FILES
from src.handle_sql import SQL_FILES


def create_storage_directories():
    storage_dirs = (HTML_FILES, SQL_FILES)
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)
