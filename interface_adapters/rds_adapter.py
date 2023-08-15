from config.settings import Settings


class RDSAdapter:
    def __init__(self, aws_session):
        self.rds = aws_session.client('rds')
        self.config = Settings().get_sql_server_config()
        self.dbInstanceIdentifier = self.config['DBInstanceIdentifier']

    def create_instance(self):
        response = self.rds.create_db_instance(**self.config)
        return response

    def delete_instance(
            self,
            skip_final_snapshot=True
            ):
        """
        Deletes an RDS instance.

        Args:
        - db_instance_identifier (str): The DB instance identifier.
        - skip_final_snapshot (bool): Determines whether a final DB snapshot
                                    is created
                                    before the DB instance is deleted.
                                    If true, no DBSnapshot is created.
                                    If false, a DB snapshot is created before
                                    deletion.

        Returns:
        - dict: Response from the RDS client.
        """
        response = self.rds.delete_db_instance(
            DBInstanceIdentifier=self.dbInstanceIdentifier,
            SkipFinalSnapshot=skip_final_snapshot
        )
        return response
