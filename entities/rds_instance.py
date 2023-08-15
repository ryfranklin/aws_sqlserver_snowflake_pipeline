from config.settings import Settings as settings


class RDSInstance:
    def __init__(self, aws_session):
        self.rds = aws_session.client('rds')
        self.config = settings.get_sql_server_config()

    def create_instance(self):
        '''
        Creates a new RDS instance
        '''
        instance = self.rds.create_db_instance(self.config)
        return instance

    def delete_instance(
            self,
            db_instance_identifier,
            skip_final_snapshot=True
            ):
        response = self.rds.delete_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            SkipFinalSnapshot=skip_final_snapshot
        )
        return response
