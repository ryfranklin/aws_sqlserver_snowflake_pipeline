from interface_adapters.rds_adapter import RDSAdapter
from config.settings import Settings


class RDSMainOperations:
    '''
    A class to manage RDS instances
    '''
    def __init__(self):
        self.rds = RDSAdapter()
        self.config = Settings().get_sql_server_config()
        self.dbInstanceIdentifier = self.config['DBInstanceIdentifier']

    def create_instance(self):
        '''
        Creates an RDS instance
        '''
        response = self.rds.create_db_instance(**self.config)
        return response

    def delete_instance(
            self,
            skip_final_snapshot=True
            ):
        '''
        Deletes an RDS instance
        '''
        response = self.rds.delete_db_instance(
            DBInstanceIdentifier=self.dbInstanceIdentifier,
            SkipFinalSnapshot=skip_final_snapshot
        )
        return response
