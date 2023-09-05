from sqlite3 import connect
from src.handle_sql.constants import DATABASE_PATH


def cursor_dec(func):
    """Creates, commits and closes a cursor around a function that should execute a SQL command."""

    def wrapper(*args, **kwargs):
        self = args[0]
        kwargs['connection'] = self.create_connection()
        kwargs['cursor'] = kwargs['connection'].cursor()
        func(*args, **kwargs)
        self.store_cursor_data(**kwargs)
        kwargs['connection'].commit()
        kwargs['cursor'].close()
        kwargs['connection'].close()

    return wrapper


class ManageConnection:

    def __init__(self, database_file=DATABASE_PATH):
        self.database = database_file
        self.temp_cursor_data: list = []

    def create_connection(self):
        return connect(self.database)

    def store_cursor_data(self, **kwargs):
        database_rows = []
        for row in kwargs['cursor']:
            database_rows.append(row)
        self.temp_cursor_data = database_rows

    def return_cursor_data(self):
        return self.temp_cursor_data

    @cursor_dec
    def cursor_execute(self, sql_command, **kwargs):
        kwargs['cursor'].execute(sql_command)

    @cursor_dec
    def cursor_executemany(self, *args, **kwargs):
        kwargs['cursor'].executemany(*args)
