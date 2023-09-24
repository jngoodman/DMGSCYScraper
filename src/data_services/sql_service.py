from src.handle_sql import HandleDatabase, CustomQueries, Queries, get_query_from_file
from typing import Union
from src.data_services.html_services import HTMLCollServ, HTMLMerchServ


class SQLService:
    """When a band name is given as a kwarg, this class will perform queries on that band's merch table, as opposed
    to the default collections table (for all bands)."""
    _database_handler: HandleDatabase
    _band_name: Union[str, None]
    _query_handler: Union[CustomQueries, None]
    _options: dict

    def __init__(self, database_file, **kwargs):
        self._options = kwargs
        self._database_handler = HandleDatabase(database_file)
        self._band_name = None
        self.run_mode = None
        self.pass_options()
        self.get_run_mode()

    def pass_options(self):
        if 'print_' in self._options:
            self._database_handler.options.update({'print_': True})
        if 'return_' in self._options:
            self._database_handler.options.update({'return_': True})

    def get_run_mode(self):
        modes_list = [{True: 'collections'},
                      {'band_name' in self._options: 'merch'},
                      {'favourites' in self._options and self._options['favourites'] == True: 'favourites'}]
        # priority is implied in the order of the list, since for loop will give us the last value
        for dictionary in modes_list:
            if any([boolean for boolean in dictionary.keys()]):
                [self.run_mode] = [run_mode for run_mode in dictionary.values()]
        if self.run_mode == 'merch':
            self._query_handler = CustomQueries(self._database_handler)
            self._band_name = self._options['band_name']

    def create_table(self):
        database_handler = self._database_handler
        query_dict = {'favourites': "Queries.CREATE_FAVOURITES_TABLE",
                      'merch': "self._query_handler.call_query(Queries.CREATE_MERCH_TABLE, self._band_name)",
                      'collections': "Queries.CREATE_BAND_TABLE"}
        return database_handler.run_command(eval(query_dict[self.run_mode]))

    def select_table(self):
        database_handler = self._database_handler
        query_dict = {'favourites': "Queries.SELECT_FAVOURITES_TABLE",
                      'merch': "self._query_handler.call_query(Queries.SELECT_MERCH_TABLE, self._band_name)",
                      'collections': "Queries.SELECT_BAND_TABLE"}
        return database_handler.run_command(eval(query_dict[self.run_mode]))

    def drop_table(self):
        database_handler = self._database_handler
        query_dict = {'favourites': "Queries.DROP_FAVOURITES_TABLE",
                      'merch': "self._query_handler.call_query(Queries.DROP_MERCH_TABLE, self._band_name)",
                      'collections': "Queries.DROP_BAND_TABLE"}
        return database_handler.run_command(eval(query_dict[self.run_mode]))

    def _get_default_fill_data(self):
        """Get default data by parsing HTML."""
        if self.run_mode == 'favourites':
            print("There is no default fill data for the favourites table. Call fill_table with *data.")
            return None
        if self.run_mode == 'merch':
            url = self.get_url_from_collections()
            data = HTMLMerchServ(self._band_name, url).return_names_images_prices_list()
        else:
            data = HTMLCollServ().return_names_urls_list()
        return data

    def add_to_table(self, *data: list):
        """Make possible to insert other list, but otherwise parse relevant HTML for intended function."""
        if not data:
            data = self._get_default_fill_data()
        database_handler = self._database_handler
        query_dict = {'favourites': "Queries.ADD_TO_FAVOURITES_TABLE",
                      'merch': "self._query_handler.call_query(Queries.ADD_TO_MERCH_TABLE, self._band_name)",
                      'collections': "Queries.ADD_TO_BAND_TABLE"}
        return database_handler.run_command(eval(query_dict[self.run_mode]), data)

    def remove_from_table(self, local_band_name):
        if self.run_mode != 'favourites':
            print("You cannot remove entries from these tables. Entries should reflect the HTML data.")
            return None
        database_handler = self._database_handler
        query = get_query_from_file(Queries.REMOVE_FROM_FAVOURITES_TABLE).format(local_band_name)
        return database_handler.run_command(query)

    def delete_database(self):
        self._database_handler.delete_database_file_on_disk()

    def get_url_from_collections(self):
        if self.run_mode == 'merch':
            database_handler = self._database_handler
            query = self._query_handler.call_query(Queries.GET_ROW_FROM_BAND, self._band_name)
            url = database_handler.run_command(query)[0][1]
            return url
        print("This function requires SQLService to be in merch mode. Please instantiate with a band name.")
