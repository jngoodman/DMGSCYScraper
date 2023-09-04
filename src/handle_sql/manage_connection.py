from sqlite3 import connect
from src.handle_sql.constants import DATABASE_PATH


def cursor(func):
    """Creates, commits and closes a cursor around a function that should execute a SQL command."""
    def wrapper(*args, **kwargs):
        self = args[0]
        if self.connection:
            self.cursor = self.connection.cursor()
            func(*args, **kwargs)
            self.connection.commit()
            self.cursor.close()

    return wrapper


class ManageConnection:

    def __init__(self):
        self.connection = None
        self.database = DATABASE_PATH
        self.cursor = None
        self.temp_cursor_data: list = []

    def create_connection(self):
        self.connection = connect(self.database)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def return_cursor_data(self):
        database_rows = []
        for row in self.cursor:
            database_rows.append(row)
        return database_rows

    @cursor
    def execute_sql_command(self, *args, many=False, get_cursor_data=False):
        if not many:
            self.cursor.execute(*args)
        else:
            self.cursor.executemany(*args)
        if get_cursor_data:
            self.temp_cursor_data = self.return_cursor_data()
