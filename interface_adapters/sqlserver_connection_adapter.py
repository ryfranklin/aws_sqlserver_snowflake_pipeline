import pyodbc


class SqlServerConnectionAdapter:
    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password

    def get_connection(self):
        conn_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};\
                    SERVER={self.server};\
                    UID={self.username};\
                    PWD={self.password};\
                    TrustServerCertificate=yes;'
        return pyodbc.connect(conn_str)
