from src.handle_sql.manage_connection import ManageConnection
from src.handle_sql.constants import DATABASE_PATH, CommandPaths
from src.handle_http import HandleLocalHTTP
from os import path


def read_sql_script(file_path):
    with open(file_path, 'r') as sql_file:
        return sql_file.read()


def connect_exec_close(func):
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
        self.local_http_handler = HandleLocalHTTP()

    @connect_exec_close
    def create_database(self):
        script_string: str = read_sql_script(CommandPaths.CREATE_DATABASE)
        if not path.isfile(DATABASE_PATH):
            self.connection_manager.execute_sql_command(script_string)

    @connect_exec_close
    def create_band_table(self):
        script_string: str = read_sql_script(CommandPaths.CREATE_BAND_TABLE)
        self.connection_manager.execute_sql_command(script_string)

    @connect_exec_close
    def add_to_band_table(self):
        script_string: str = read_sql_script(CommandPaths.ADD_TO_BAND_TABLE)
        rows_to_insert = []
        self.local_http_handler.run()
        for band, url in self.local_http_handler.bands_dictionary.items():
            rows_to_insert.append([band, url])
        self.connection_manager.execute_sql_command(script_string, rows_to_insert, many=True)


