from src.handle_sql import HandleDatabase


class DatabaseService:
    _database_handler: HandleDatabase

    def __init__(self, database_file: str):
        self._database_handler = HandleDatabase(database_file, return_=True)

    def read_data_from_query(self, query_key: str, *args):
        database_handler = self._database_handler
        db_data = database_handler.run_command(query_key=query_key, *args)
        return db_data


class BandCollectionsDatabaseService(DatabaseService):

    def __init__(self, database_file: str):
        super().__init__(database_file)

    def get_url_by_band(self, query_key: str, *args):
        # temp response to be updated
        print(self.read_data_from_query(query_key, *args))
