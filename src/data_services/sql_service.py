from src.handle_sql import HandleDatabase, CustomQueries, Queries
from typing import Union


class SQLService:
    """When a band name is given as a kwarg, this class will perform queries on that band's merch table, as opposed
    to the default collections table (for all bands)."""
    _database_handler: HandleDatabase
    _band_name: Union[str, None]
    _query_handler: Union[CustomQueries, None]
    _options: dict

    def __init__(self, database_file, **kwargs):
        self._options = kwargs
        self._database_handler = HandleDatabase(database_file,
                                                return_=kwargs['return_'],
                                                print_=kwargs['print_'])
        self._band_name = None
        self.construct_conditional_arguments()

    def construct_conditional_arguments(self):
        if 'band_name' in self._options:
            self._band_name = self._options['band_name']
            self._query_handler = CustomQueries(self._database_handler)

    def create_table(self):
        database_handler = self._database_handler
        if self._band_name:
            query = self._query_handler.call_query(Queries.Partial.CREATE_MERCH_TABLE, self._band_name)
        else:
            query = Queries.CREATE_BAND_TABLE
        return database_handler.run_command(query)

    def select_table(self):
        database_handler = self._database_handler
        if self._band_name:
            query = self._query_handler.call_query(Queries.Partial.SELECT_MERCH_TABLE, self._band_name)
        else:
            query = Queries.SELECT_BAND_TABLE
        return database_handler.run_command(query)

    def drop_table(self):
        database_handler = self._database_handler
        if self._band_name:
            query = self._query_handler.call_query(Queries.Partial.DROP_MERCH_TABLE, self._band_name)
        else:
            query = Queries.DROP_BAND_TABLE
        return database_handler.run_command(query)

    def fill_table(self, data: list):
        database_handler = self._database_handler
        if self._band_name:
            query = self._query_handler.call_query(Queries.Partial.ADD_TO_MERCH_TABLE, self._band_name)
        else:
            query = Queries.ADD_TO_BAND_TABLE
        return database_handler.run_command(query, data)

    def get_url_from_collections(self):
        if self._band_name:
            database_handler = self._database_handler
            query = self._query_handler.call_query(Queries.Partial.GET_ROW_FROM_BAND, self._band_name.title())
            url = database_handler.run_command(query)[0][1]
            return url
        print("SQLService was not instantiated with a band name.")
