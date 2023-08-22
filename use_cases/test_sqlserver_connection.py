class TestSqlServerConnection:
    def __init__(self, connection):
        self.sql_connection = connection

    def execute(self):
        # Fetch the version of the SQL Server instance
        cursor = self.sql_connection.cursor()
        cursor.execute('SELECT @@version;')
        version = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        self.sql_connection.close()

        return version[0]
