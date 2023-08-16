from interface_adapters.sqlserver_adapter import (
    SqlServerConnectionAdapter
)
from frameworks_and_drivers.database_operations import (
    DatabaseInitializer
)


class CreateDatabaseAndOrdersTable:
    def __init__(self):
        self.db_adapter = SqlServerConnectionAdapter()
        self.db_initializer = DatabaseInitializer(self.db_adapter)

    def create_database(self):
        self.db_initializer.create_database('ecommerce-db')

    def switch_database(self):
        self.db_adapter.database = 'ecommerce-db'

    def create_orders_table(self):
        self.db_initializer.create_orders_table()
