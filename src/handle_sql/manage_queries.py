from src.handle_sql.constants import Queries
from src.handle_sql.manage_sql_database import HandleDatabase, get_query_from_file


class CustomQueries:
    _database_handler: HandleDatabase
    _allowed_inputs: list

    def __init__(self, database_handler: HandleDatabase):
        """The only allowed inputs will be band names in the database being accessed. The user should be able to create
        custom inputs of the following kinds:
        (1) Row selection from band name: USER INPUTS f"'{band_name}'" to SELECT query.
        (2) Merch table creation from band name. USER INPUTS f"'{band_name}'" to CREATE TABLE query."""
        self._database_handler = database_handler
        self._allowed_inputs = self._database_handler.run_command(query=Queries.SELECT_NAME_BAND_TABLE)

    def call_query(self, partial_query_path: str, variable_name: str):
        allowed_inputs = [tuple_[0].lower() for tuple_ in self._allowed_inputs]
        partial_query = get_query_from_file(partial_query_path)
        if variable_name.lower() in allowed_inputs:
            full_query = partial_query.format(variable_name)
            return full_query
        print("Band name not found in bands database.")


