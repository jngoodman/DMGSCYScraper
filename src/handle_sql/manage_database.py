from src.handle_sql.manage_connection import ManageConnection
from src.handle_sql.constants import DATABASE_PATH, CommandPaths
from src.handle_html import HandleBandHTML
from os import remove


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


class HandleDatabase:
    """Handle a database file. Specifies an input database path and an input html_handler. The html_handler is used
    to access data from different locally-stored html files. For DMGSCY data, a unique html_file exists for the band
    collections page, and any specific band collections that have been requested by the user."""

    def __init__(self, database_file=DATABASE_PATH, html_handler=HandleBandHTML()):
        self.database_file = database_file
        self.connection_manager = ManageConnection(database_file)
        self.html_handler = html_handler

    def execute_basic_command(self, sql_path=CommandPaths.CREATE_BAND_TABLE):
        """Executes a SQL command without accepting additional parameters. Acceptable commands:
        CREATE_BAND_TABLE: creates band table.
        SELECT_BAND_TABLE: selects all in band table."""
        connection_manager = self.connection_manager
        command: str = read_file(sql_path)
        connection_manager.cursor_execute(command)

    def execute_print_command(self, sql_path=CommandPaths.SELECT_BAND_TABLE):
        """Executes a SQL command without accepting additional parameters and prints into python. Acceptable commands:
        SELECT_BAND_TABLE: selects all in band table."""
        connection_manager = self.connection_manager
        command: str = read_file(sql_path)
        connection_manager.cursor_execute(command)
        print(connection_manager.temp_cursor_data)

    def delete_database_file_on_disk(self):
        user_response = input("This will delete the database on disk. Do you want to do this? (Y/N). ").lower()
        if user_response == 'y':
            print("Database deleted.")
            remove(self.database_file)
        else:
            print("Deletion aborted.")

    def execute_insertion_command(self, sql_path=CommandPaths.ADD_TO_BAND_TABLE):
        """Executes a SQL command to insert html data into a table. Acceptable commands:
        ADD_TO_BAND_TABLE: adds band name and url rows to band table."""
        connection_manager = self.connection_manager
        command: str = read_file(sql_path)
        rows_to_insert = []
        self.html_handler.run()
        for band, url in self.html_handler.bands_dictionary.items():
            rows_to_insert.append([band, url])
        connection_manager.cursor_executemany(command, rows_to_insert)
