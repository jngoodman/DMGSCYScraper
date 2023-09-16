from src import HandleDatabase, GetHTML, Queries, DMGSCY_PATH, BandCollectionsHTMLService, \
    BAND_COLLECTIONS_URL, CustomQueries, BandCollectionsSQLService, BandMerchSQLService, BAND_COLLECTIONS_FILENAME, \
    gen_html_filename, BandMerchHTMLService
from os import path, makedirs


def create_storage_directories():
    storage_dirs = (r"src/pull_html/html_files/", r"src/handle_sql/sql_database/")
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def test_bands_table(print_: bool):
    html_service = BandCollectionsHTMLService()
    html_service.html_getter.check_if_file_exists()
    db_service = BandCollectionsSQLService(database_file=DMGSCY_PATH, print=print_)
    db_service.create_band_table()
    db_service.fill_band_table()
    db_service.select_band_table()


def test_merch_table(print_: bool):
    db_merch_service = BandMerchSQLService(database_file=DMGSCY_PATH, print=print_, band_name='Green Day')
    db_merch_service.create_merch_table()
    db_merch_service.select_merch_table()
    db_merch_service.drop_merch_table()


def test_get_merch_html(print_: bool):
    db_service = BandCollectionsSQLService(database_file=DMGSCY_PATH, print=print_)
    url = db_service.get_url_by_band('Green Day')
    html_service = BandMerchHTMLService('Green Day', url)
    html_service.html_getter.check_if_file_exists()
    print(html_service.return_product_names())
    print(html_service.return_product_prices())
    print(html_service.return_product_images())


def main():
    create_storage_directories()
    user_input = input("DEVELOPMENT. Would you like to test the bands table? (Y/N): ").lower()
    if user_input == 'y':
        test_bands_table(print_=True)
    user_input = input("DEVELOPMENT. Would you like to test a merch table? (Y/N): ").lower()
    if user_input == 'y':
        test_merch_table(print_=True)
    user_input = input("DEVELOPMENT. Would you like to test a merch html? (Y/N): ").lower()
    if user_input == 'y':
        test_get_merch_html(print_=True)


if __name__ == "__main__":
    main()
