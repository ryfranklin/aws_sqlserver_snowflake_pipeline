# from interface_adapters import rds_adapter
from frameworks_and_drivers.aws_session import AwsSession
from interface_adapters.rds_adapter import RDSAdapter
from interface_adapters.s3_adapter import S3Adapter
from scripts.initialize_database import CreateDatabaseAndOrdersTable


class MainApp:

    def __init__(self):
        # Initialize the AWS session
        self.session = AwsSession().get_aws_session()
        # Initialize the RDS adapter
        self.rds_adapter = RDSAdapter(self.session)
        # initialize the S3 adapter
        self.s3_adapter = S3Adapter(self.session)

    def run(self):
        creator = CreateDatabaseAndOrdersTable()
        creator.create_database()
        creator.switch_database()
        creator.create_orders_table()
        # print("==================================")
        # print("Creating RDS instance...")
        # self.rds_adapter.create_instance()
        # print("RDS instance created successfully!")
        # print("==================================")
        # print("Creating S3 bucket...")
        # self.s3_adapter.create_bucket('ms3dm-test-bronze-bucket')
        # print("S3 bucket created successfully!")
        # print("==================================")
        # print("==================================")
        # print("List S3 buckets...")
        # buckets = self.s3_adapter.list_buckets()
        # for bucket in buckets['Buckets']:
        #     print(bucket['Name'])
        # print("==================================")

    # def rds_create_operations(self):
    #     # Create Session
    #     rds = rds_adapter.RDSAdapter(self.session)
    #     print(rds)
    #     print(self.config)
    #     # Configuration for RDS instance

    #     # Create RDS instance
    #     instance_response = rds.create_instance(rds_config)
    #     print(instance_response)

    #     # Here, you can add other RDS related operations or methods if
    #           needed.

    # def rds_return_session_operations(self):
    #     # Return session
    #     rds = rds_adapter.RDSAdapter(self.session)
    #     print(rds.return_session())


if __name__ == "__main__":
    app = MainApp()
    app.run()
