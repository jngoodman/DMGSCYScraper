from src.handle_sql import HandleDatabase, CustomQueries, Queries


class SQLService:

    def __init__(self, database_file: str):
        self._database_handler = HandleDatabase(database_file, return_=True)
        self._allowed_inputs = self._database_handler.run_command(query_path=Queries.SELECT_NAME_BAND_TABLE)

    def get_url_by_band(self, band_name: str):
        database_handler = self._database_handler
        allowed_inputs = [tuple_[0].lower() for tuple_ in self._allowed_inputs]
        if band_name.lower() in allowed_inputs:
            query = CustomQueries().call_query_path('get_row_from_band', band_name)
            url = database_handler.run_command(query)[0][1]
            return url
        print("Invalid variable name.")



