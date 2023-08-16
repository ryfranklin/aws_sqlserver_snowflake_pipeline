from entities.glue_entities import GlueJob, OrdersTable


class CreateAndPopulateOrdersTable:
    """Use Case: Create and Populate Orders Table using Glue."""

    def __init__(self, glue_job: GlueJob, orders_table: OrdersTable):
        self.glue_job = glue_job
        self.orders_table = orders_table

    def execute(self):
        self.glue_job.create()
        self.glue_job.start()
        self.orders_table.create()
        self.orders_table.populate()
        self.glue_job.wait_for_completion()
        self.glue_job.stop()
        self.glue_job.delete()
