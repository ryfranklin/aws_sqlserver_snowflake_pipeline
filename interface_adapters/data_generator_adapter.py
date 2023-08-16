from faker import Faker
from entities.glue_entities import Order


class FakeDataGeneratorAdapter:
    def __init__(self):
        self.faker = Faker()

    def generate_orders(self, n_records):
        orders = []
        for _ in range(n_records):
            order_data = Order(
                self.faker.uuid4(),
                self.faker.product_name(),
                self.faker.random_number(digits=2),
                self.faker.name(),
                self.faker.address(),
                self.fkaer.date()
            )
            orders.append(order_data)
        return orders
