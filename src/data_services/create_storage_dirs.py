from os import path, makedirs
from src.data_services.constants import Dirs


def create_storage_directories():
    storage_dirs = (Dirs.HTML_FILES, Dirs.SQL_FILES)
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)
