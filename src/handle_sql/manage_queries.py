from src.handle_sql.constants import QueryBases, DMGSCY_PATH, Queries, CUSTOM_COMMANDS_PATH
from src.handle_sql.manage_database import HandleDatabase, get_query_from_file


class CustomQueries:
    """Class is deliberately hard-coded to prevent SQL injection."""
    _database_handler: HandleDatabase
    _allowed_inputs: list

    def __init__(self):
        """The only allowed inputs will be band names in the database being accessed. The user should be able to create
        custom inputs of the following kinds:
        (1) Row selection from band name: USER INPUTS f"'{band_name}'" to SELECT query.
        (2) Merch table creation from band name. USER INPUTS f"'{band_name}'" to CREATE TABLE query."""
        self._database_handler = HandleDatabase(database_file=DMGSCY_PATH, return_=True)
        self._allowed_inputs = self._database_handler.run_command(query_key=Queries.SELECT_NAME_BAND_TABLE)

    def create_query_file(self, partial_query_key: str, variable_name: str):
        allowed_inputs = [tuple_[0].lower() for tuple_ in self._allowed_inputs]
        partial_query = get_query_from_file(QueryBases[partial_query_key])
        if variable_name.lower() in allowed_inputs:
            full_query = partial_query.format(variable_name)
            file_name = f"{CUSTOM_COMMANDS_PATH}{partial_query_key}_{variable_name.lower()}"
            with open(f'{file_name}.sql', 'w') as file:
                file.write(full_query)
        else:
            print("Invalid variable name.")

