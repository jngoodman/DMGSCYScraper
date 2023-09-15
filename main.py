from src import HandleDatabase, GetHTML, Queries, DMGSCY_PATH, BandCollectionsHTMLService, \
    BAND_COLLECTIONS_URL, CustomQueries, SQLService, BAND_COLLECTIONS_FILENAME, gen_html_filename, BandMerchHTMLService
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
    html = GetHTML(url=BAND_COLLECTIONS_URL, file_name=BAND_COLLECTIONS_FILENAME)
    html.check_if_file_exists()
    manage_database = HandleDatabase(database_file=DMGSCY_PATH, print=_print)
    for list_ in param_list:
        manage_database.run_command(*[param for param in list_])
    manage_database.delete_database_file_on_disk()


def test_merch_table(_print: bool):
    manage_database = HandleDatabase(database_file=DMGSCY_PATH, print=_print)
    create_merch_path = CustomQueries().call_query_path('create_merch_table', 'Green Day')
    select_merch_path = CustomQueries().call_query_path('select_merch_table', 'Green Day')
    drop_merch_path = CustomQueries().call_query_path('drop_merch_table', 'Green Day')
    manage_database.run_command(create_merch_path)
    manage_database.run_command(select_merch_path)
    manage_database.run_command(drop_merch_path)


def test_get_merch_html():
    url = SQLService(database_file=DMGSCY_PATH).get_url_by_band('Green Day')
    html = GetHTML(url=url, file_name=gen_html_filename('Green Day'))
    html.check_if_file_exists()
    print(BandMerchHTMLService(band_name='Green Day').return_product_names())
    print(BandMerchHTMLService(band_name='Green Day').return_product_prices())
    print(BandMerchHTMLService(band_name='Green Day').return_product_images())


def main():
    create_storage_directories()
    user_input = input("DEVELOPMENT. Would you like to test the bands table? (Y/N): ").lower()
    if user_input == 'y':
        test_bands_table(_print=True)
    user_input = input("DEVELOPMENT. Would you like to test a merch table? (Y/N): ").lower()
    if user_input == 'y':
        test_merch_table(_print=True)
    user_input = input("DEVELOPMENT. Would you like to test a merch html? (Y/N): ").lower()
    if user_input == 'y':
        test_get_merch_html()


if __name__ == "__main__":
    main()
