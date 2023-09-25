from os import path, makedirs, remove
from src.pull_html import HTML_FILES
from src.handle_sql import SQL_FILES
from glob import glob
from src.data_services.constants import TEMP


def create_storage_directories():
    storage_dirs = (HTML_FILES, SQL_FILES)
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def clear_temp(folder: str = TEMP):
    files = glob(f"{folder}*")
    for file in files:
        remove(file)
