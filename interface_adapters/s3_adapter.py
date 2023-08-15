import boto3


class S3Adapter:
    def __init__(self, aws_session):
        self.s3 = aws_session.client('s3')

    def create_bucket(self, bucket_name):
        response = self.s3.create_bucket(Bucket=bucket_name)
        return response

    def list_buckets(self):
        response = self.s3.list_buckets()
        return response

    def upload(self, file_name, file_path):
        s3 = boto3.client('s3')
        s3.upload_file(file_path, self.bucket_name, file_name)
