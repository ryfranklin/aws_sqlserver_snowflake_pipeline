import pyodbc


class DatabaseConnectionAdapter:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

    def get_connection(self):
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};\
                    SERVER={self.server};DATABASE={self.database};\
                    UID={self.username};\
                    PWD={self.password}'
        return pyodbc.connect(conn_str)
