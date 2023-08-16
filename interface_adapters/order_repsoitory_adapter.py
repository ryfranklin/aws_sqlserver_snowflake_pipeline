class OrderRepositoryAdapter:
    def __init__(self, order):
        # using a relational database
        with self.connection.cursor() as cursor:
            sql = """
                    INSERT INTO Orders(
                        order_id,
                        product_name,
                        price,
                        customer_name,
                        address,
                        order_date
                    )
                    VALUES(%s, %s, %s, %s, %s, %s)
                """
            cursor.execute(sql, (order.order_id,
                                 order.product_name,
                                 order.price,
                                 order.customer_name,
                                 order.address,
                                 order.order_date))
