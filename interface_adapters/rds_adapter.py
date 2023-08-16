class RDSAdapter:
    def __init__(self, aws_session):
        self.rds = aws_session.client('rds')

    def create_session(self):
        return self.rds
