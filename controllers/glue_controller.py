from use_cases.glue_create_and_populate_orders_table import (
    CreateAndPopulateOrdersTable
)
from interface_adapters.glue_adapter import GlueAdapter


class GlueController:

    def __init__(self):
        self.glue_adapter = GlueAdapter()
        self.create_and_populate_orders_table = CreateAndPopulateOrdersTable(
            glue_job=self.glue_adapter,
            orders_table=self.glue_adapter
        )

    def setup_orders_table(
            self,
            job_name,
            script_location,
            n_records
    ):
        self.use_case.execute(
            job_name,
            script_location,
            n_records
        )
