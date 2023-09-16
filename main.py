from src.handle_sql import DMGSCY_PATH
from src.data_services import CollectionsHTMLService, SQLService, MerchHTMLService
from os import path, makedirs


def create_storage_directories():
    storage_dirs = (r"src/pull_html/html_files/", r"src/handle_sql/sql_database/")
    for dir_ in storage_dirs:
        if not path.exists(dir_):
            makedirs(dir_)


def main():
    create_storage_directories()
    service = SQLService(database_file=DMGSCY_PATH, print_=True, return_=True)
    service.create_table()
    service.fill_table(data=CollectionsHTMLService().return_names_urls_list())
    service.select_table()
    new_service = SQLService(database_file=DMGSCY_PATH, print_=True, return_=True, band_name='Green Day')
    new_service.create_table()
    url = new_service.get_url_from_collections()
    # this isn't ideal - need an interface to talk between the SQL service and HTML service
    # also: consider simplifying HTML service into one
    new_service.fill_table(data=MerchHTMLService('Green Day', url).return_names_images_prices_list())
    new_service.select_table()


if __name__ == "__main__":
    main()
