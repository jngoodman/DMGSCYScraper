from src import HandleDatabase, GetHTML, Queries, HTML_KEYS, DMGSCY_PATH, BandCollectionsHTMLService, \
    BAND_COLLECTIONS_URL, BandCollectionsDatabaseService, CustomQueries
from os import path, makedirs


def create_storage_directories():
    storage_dirs = (r"src/pull_html/html_files/", r"src/handle_sql/sql_database/")
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def test_bands_table(_print: bool):
    param_list = [
        [Queries.CREATE_BAND_TABLE],
        [Queries.ADD_TO_BAND_TABLE, BandCollectionsHTMLService().return_names_urls_list()],
        [Queries.SELECT_BAND_TABLE],
    ]
    html = GetHTML(url=BAND_COLLECTIONS_URL, html_key=HTML_KEYS['band_collections'])
    html.check_if_file_exists()
    # with a new database service now on top of the handler, good practice could be to use the service instead
    # that being said, the purpose of the service is to pass around data from sql and python - sometimes you just want
    # to make a sql database, and don't need to read or return that data in python
    manage_database = HandleDatabase(database_file=DMGSCY_PATH, print=_print)
    for list_ in param_list:
        manage_database.run_command(*[param for param in list_])
    manage_database.delete_database_file_on_disk()


def test_merch_table():
    test = BandCollectionsDatabaseService(DMGSCY_PATH)
    pass


def test_write_sql():
    CustomQueries().create_query_file('get_row_from_band', 'Green Day')
    CustomQueries().create_query_file('create_merch_table', 'Green Day')


def main():
    create_storage_directories()
    user_input = input("DEVELOPMENT. Would you like to test the bands table? (Y/N): ").lower()
    if user_input == 'y':
        test_bands_table(_print=True)
    user_input = input("DEVELOPMENT. Would you like to test a merch table? (Y/N): ").lower()
    if user_input == 'y':
        test_merch_table()
    user_input = input("DEVELOPMENT. Would you like to test custom queries? (Y/N): ").lower()
    if user_input == 'y':
        test_write_sql()


if __name__ == "__main__":
    main()
