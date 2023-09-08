from src.handle_sql import HandleDatabase, CustomQueries
from pandas import DataFrame


class DatabaseService:
    _database_handler: HandleDatabase

    def __init__(self, database_file: str):
        """The purpose of DatabaseService is to (1) instantiate a database handler with return_=True to extract values
        from sql databases and (2) to perform .db specific operations on this data."""
        self._database_handler = HandleDatabase(database_file, return_=True)

    def read_data_from_query(self, query_key: str, *args):
        """Because return_=True in database_handler(), then .run_command returns the cursor data."""
        database_handler = self._database_handler
        return database_handler.run_command(query_key=query_key, *args)


class BandCollectionsDatabaseService(DatabaseService):

    def __init__(self, database_file: str):
        super().__init__(database_file)
