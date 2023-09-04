from src.handle_sql.manage_connection import ManageConnection
from src.handle_sql.constants import DATABASE_PATH, CommandPaths
from src.handle_html import HandleLocalHTML
from os import path


def read_sql_script(file_path):
    with open(file_path, 'r') as sql_file:
        return sql_file.read()


def connect_exec_close(func):
    """Creates and closes a database connection around a function that should execute a SQL command to the connection
    manager of a ManageDatabase instance."""

    def wrapper(*args):
        self = args[0]
        self.connection_manager.create_connection()
        func(*args)
        self.connection_manager.close_connection()

    return wrapper


class ManageDatabase:

    def __init__(self):
        self.connection_manager = ManageConnection()
        self.database = self.connection_manager.database
        self.local_html_handler = HandleLocalHTML()

    @connect_exec_close
    def create_database(self):
        script_string: str = read_sql_script(CommandPaths.CREATE_DATABASE)
        if not path.isfile(DATABASE_PATH):
            self.connection_manager.execute_sql_command(script_string)

    @connect_exec_close
    def create_table(self, command=CommandPaths.CREATE_BAND_TABLE):
        """Creates a table. Default is the band table."""
        script_string: str = read_sql_script(command)
        self.connection_manager.execute_sql_command(script_string)

    @connect_exec_close
    def return_table(self, command=CommandPaths.RETURN_BAND_TABLE):
        """Returns a table. Default is the band table."""
        script_string: str = read_sql_script(command)
        self.connection_manager.execute_sql_command(script_string, get_cursor_data=True)
        print(self.connection_manager.temp_cursor_data)

    @connect_exec_close
    def add_to_band_table(self):
        script_string: str = read_sql_script(CommandPaths.ADD_TO_BAND_TABLE)
        rows_to_insert = []
        self.local_html_handler.run()
        for band, url in self.local_html_handler.bands_dictionary.items():
            rows_to_insert.append([band, url])
        self.connection_manager.execute_sql_command(script_string, rows_to_insert, many=True)


