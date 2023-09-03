from sqlite3 import connect
from src.handle_sql.constants import DATABASE_PATH


class ManageConnection:

    def __init__(self):
        self.connection = None
        self.database = DATABASE_PATH

    def create_connection(self):
        self.connection = connect(self.database)

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def execute_sql_command(self, *args, many=False):
        if self.connection:
            cursor = self.connection.cursor()
            if not many:
                cursor.execute(*args)
            else:
                cursor.executemany(*args)
            self.connection.commit()
            cursor.close()
