class DatabaseOperations:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter

    def create_database(self, database_name):
        with self.db_adapter.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE {database_name}")
            conn.commit()

    def create_orders_table(self):
        with self.db_adapter.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE Orders (
                    order_id NVARCHAR(255) PRIMARY KEY,
                    product_name NVARCHAR(255),
                    price DECIMAL(10, 2),
                    customer_name NVARCHAR(255),
                    address NVARCHAR(500),
                    order_date DATE
                )
            """)
            conn.commit()
