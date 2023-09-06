from src import HandleDatabase, check_for_local_data, Queries, HTML_KEYS, DMGSCY_PATH, BandCollectionsService
from os import path, makedirs


def create_storage_directories():
    storage_dirs = (r"src/handle_html/html_files/", r"src/handle_sql/sql_database/")
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def main():
    create_storage_directories()
    check_for_local_data(path_=HTML_KEYS['band_collections'])
    manage_database = HandleDatabase(database_file=DMGSCY_PATH, print=True)
    manage_database.run_command(Queries.CREATE_BAND_TABLE)
    manage_database.run_command(Queries.ADD_TO_BAND_TABLE, BandCollectionsService().return_names_urls_list())
    manage_database.run_command(Queries.SELECT_BAND_TABLE)
    manage_database.run_command(Queries.DROP_BAND_TABLE)
    manage_database.delete_database_file_on_disk()


if __name__ == "__main__":
    main()
