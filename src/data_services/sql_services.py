from src.handle_sql import HandleDatabase, CustomQueries, Queries
from src.data_services.html_services import CollectionsHTMLService, MerchHTMLService


class CollectionsSQLService:
    _database_handler: HandleDatabase
    _query_handler: CustomQueries

    def __init__(self, database_file: str, return_=True, **kwargs):
        self._database_handler = HandleDatabase(database_file, return_=return_, **kwargs)
        self._query_handler = CustomQueries(self._database_handler)

    def create_band_table(self):
        database_handler = self._database_handler
        database_handler.run_command(Queries.CREATE_BAND_TABLE)

    def select_band_table(self):
        database_handler = self._database_handler
        database_handler.run_command(Queries.SELECT_BAND_TABLE)

    def fill_band_table(self, data: list):
        database_handler = self._database_handler
        database_handler.run_command(Queries.ADD_TO_BAND_TABLE, data)

    def drop_band_table(self):
        database_handler = self._database_handler
        database_handler.run_command(Queries.DROP_BAND_TABLE)

    def get_url_by_band(self, band_name: str):
        database_handler = self._database_handler
        query_handler = self._query_handler
        query = query_handler.call_query(Queries.Partial.GET_ROW_FROM_BAND, band_name)
        url = database_handler.run_command(query)[0][1]
        return url


class MerchSQLService:
    _database_handler: HandleDatabase
    _query_handler: CustomQueries
    band_name: str

    def __init__(self, database_file: str, band_name: str, return_=True, **kwargs):
        self._database_handler = HandleDatabase(database_file, return_=return_, **kwargs)
        self._query_handler = CustomQueries(self._database_handler)
        self.band_name = band_name.lower()

    def create_merch_table(self):
        query_handler = self._query_handler
        database_handler = self._database_handler
        query_call = query_handler.call_query(Queries.Partial.CREATE_MERCH_TABLE, self.band_name)
        database_handler.run_command(query_call)

    def select_merch_table(self):
        query_handler = self._query_handler
        database_handler = self._database_handler
        query_call = query_handler.call_query(Queries.Partial.SELECT_MERCH_TABLE, self.band_name)
        database_handler.run_command(query_call)

    def drop_merch_table(self):
        query_handler = self._query_handler
        database_handler = self._database_handler
        query_call = query_handler.call_query(Queries.Partial.DROP_MERCH_TABLE, self.band_name)
        database_handler.run_command(query_call)

    def fill_merch_table(self, data: list):
        query_handler = self._query_handler
        database_handler = self._database_handler
        query_call = query_handler.call_query(Queries.Partial.ADD_TO_MERCH_TABLE, self.band_name)
        database_handler.run_command(query_call, data)
