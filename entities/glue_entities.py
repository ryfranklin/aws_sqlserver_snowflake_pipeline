class GlueJob:
    """Entity representing an AWS Glue Job."""
    ...


class OrdersTable:
    """Entity representing an Orders Table."""
    ...


class Order:
    def __init__(
            self,
            order_id,
            product_name,
            price,
            customer_name,
            address,
            order_date
                 ):
        self.order_id = order_id,
        self.product_name = product_name,
        self.price = price,
        self.customer_name = customer_name,
        self.address = address,
        self.order_date = order_date
