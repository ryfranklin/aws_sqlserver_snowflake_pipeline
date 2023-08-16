class S3Adapter:
    def __init__(self, aws_session):
        self.s3 = aws_session.client('s3')

    def create_s3_session(self):
        return self.s3
