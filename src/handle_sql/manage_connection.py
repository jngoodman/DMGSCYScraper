from sqlite3 import connect, OperationalError, ProgrammingError


def _catch_operational_error(func):
    def try_func(*args):
        try:
            func(*args)
        except OperationalError:
            print("ERROR: SQLite operational error. Check table exists.")
        except ProgrammingError:
            print("ERROR: SQLite programming error. Check data supplied.")

    return try_func


class ManageConnection:

    def __init__(self, database_file: str):
        self.database = database_file
        self.temp_cursor_data: list = []

    def create_connection(self):
        return connect(self.database)

    def store_cursor_data(self, cursor):
        database_rows = []
        for row in cursor:
            database_rows.append(row)
        self.temp_cursor_data = database_rows

    def return_cursor_data(self):
        return self.temp_cursor_data

    def _store_commit_close(self, connection, cursor):
        self.store_cursor_data(cursor)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def _execute(cursor, query, *args):
        if args:
            cursor.executemany(query, *args)
        else:
            cursor.execute(query)

    @_catch_operational_error
    def execute_query(self, query, *args):
        connection = self.create_connection()
        cursor = connection.cursor()
        self._execute(cursor, query, *args)
        self._store_commit_close(connection, cursor)
