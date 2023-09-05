from src import HandleDatabase, check_for_local_data, CommandPaths, BAND_COLLECTIONS_PATH
from os import path, makedirs


def create_storage_directories():
    storage_dirs = (r"src/handle_html/html_files/", r"src/handle_sql/sql_database/")
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def main():
    create_storage_directories()
    check_for_local_data(path_=BAND_COLLECTIONS_PATH)
    manage_database = HandleDatabase()
    manage_database.execute_basic_command(sql_path=CommandPaths.CREATE_BAND_TABLE)
    manage_database.execute_insertion_command(sql_path=CommandPaths.ADD_TO_BAND_TABLE)
    manage_database.execute_print_command(sql_path=CommandPaths.SELECT_BAND_TABLE)
    manage_database.execute_basic_command(sql_path=CommandPaths.DROP_BAND_TABLE)
    manage_database.delete_database_file_on_disk()


if __name__ == "__main__":
    main()
