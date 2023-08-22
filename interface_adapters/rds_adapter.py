class RDSAdapter:
    def __init__(self, aws_session):
        self.aws_session = aws_session
        self.rds_client = None

    def _create_rds_client(self):
        self.rds_client = self.aws_session.client('rds')

    def get_rds_client(self):
        self._create_rds_client()
        return self.rds_client
