from src.handle_sql import DMGSCY_PATH
from src.data_services import CollectionsHTMLService, CollectionsSQLService, MerchSQLService, MerchHTMLService
from os import path, makedirs
from sqlite3 import OperationalError

"""Flask application should automatically:
    > Create storage directories.
    > Instantiate collections table.
    > Requests collections .html from DMGSCY.co.uk.
    > Populate the bands table with this .html data.
    Users should have a button for each band that lets them:
    > Request HTML, instantiate merch table, populate merch table and select (i.e, show in Flask) table in a single click.
    Once a table already exists, users should:
    > Have a tickbox for 'use existing data' to prevent making new requests.
    > If ticked, just select table. Otherwise, do as before.
    Users should also have a button for each band that lets them:
    > Add to a favourites list.
    Finally, users should be able to:
    > Delete data from database (i.e., drop table). <issues warning>
    > Delete database itself. <issues warning>
    
    Effective way to do this: When user first loads the app, they're prompted to pick their favourite bands from the
    list. These are then saved. On future loads, user can select existing bands or 'add new favourites.'
    
    So first goal for tomorrow - get a flask application going that displays:
    > All band names from DMGSCY.
    > Lets the user add them to a list called 'favourites'.
    > Displays 'favourites list' after clicking 'submit'.
    > On all future loads, displays favourites list with 'modify' at the bottom."""


def create_storage_directories():
    storage_dirs = (r"src/pull_html/html_files/", r"src/handle_sql/sql_database/")
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def instantiate_collections(database_file=DMGSCY_PATH):
    if not path.isfile(database_file):
        db_service = CollectionsSQLService(database_file)
        db_service.create_bands_table()


def populate_collections_from_html(database_file=DMGSCY_PATH, html_service=CollectionsHTMLService()):
    try:
        db_service = CollectionsSQLService(database_file)
        db_service.fill_bands_table(html_service.return_names_urls_list())
    except OperationalError:
        print("SQLite Operational Error. Check if collections instantiated.")


def get_collection_url(band_name: str, database_file=DMGSCY_PATH):
    db_service = CollectionsSQLService(database_file)
    url = db_service.get_url_by_band(band_name)
    return url


def instantiate_merch_table(band_name: str, database_file=DMGSCY_PATH):
    db_service = MerchSQLService(database_file, band_name)
    db_service.create_merch_table()


def populate_merch_table_from_html(band_name, database_file=DMGSCY_PATH):
    band_url = get_collection_url(band_name)
    html_service = MerchHTMLService(band_name, band_url)
    html_service.html_getter.overwrite_html()
    db_service = MerchSQLService(database_file, band_name)
    db_service.fill_merch_table(html_service.return_names_images_prices_list())


def select_merch_table(band_name, database_file=DMGSCY_PATH):
    db_service = MerchSQLService(database_file, band_name)
    db_service.select_merch_table()


def select_collections_table(database_file=DMGSCY_PATH):
    db_service = CollectionsSQLService(database_file)
    db_service.select_bands_table()

