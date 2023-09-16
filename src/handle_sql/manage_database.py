from src.handle_sql.manage_connection import ManageConnection
from os import remove


def get_query_from_file(query_path):
    with open(query_path, 'r') as file:
        return file.read()


class HandleDatabase:
    _options: dict
    _database_file: str
    _connection: ManageConnection

    def __init__(self, database_file: str, **kwargs):
        self._database_file = database_file
        self._connection = ManageConnection(self._database_file)
        self._options = kwargs

    def run_command(self, query_path: str, *args):
        query: str = get_query_from_file(query_path)
        connection_manager = self._connection
        connection_manager.execute_query(query, *args)
        return self._run_options(query, connection_manager)

    def delete_database_file_on_disk(self):
        remove(self._database_file)

    def _print_query_cursor(self, query, cursor_data):
        if "print" in self._options and self._options["print"] == True:
            print(f"QUERY: {query}")
            if cursor_data:
                print(f"CURSOR_DATA: {cursor_data}")

    def _return_cursor(self, cursor_data):
        if "return_" in self._options and self._options["return_"] == True:
            return cursor_data

    def _run_options(self, query, connection_manager):
        cursor_data = connection_manager.temp_cursor_data
        self._print_query_cursor(query, cursor_data)
        return self._return_cursor(cursor_data)
