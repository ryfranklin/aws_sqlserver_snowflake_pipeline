class PopulateOrdersTable:
    def __init__(self, order_repository, data_generator):
        self.order_repository = order_repository
        self.data_generator = data_generator

    def execute(self, n_records):
        orders = self.data_generator.generate_orders(n_records)
        self.order_repository.save_orders(orders)
