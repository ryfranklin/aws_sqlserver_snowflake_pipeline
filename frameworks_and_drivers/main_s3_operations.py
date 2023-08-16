from interface_adapters.s3_adapter import S3Adapter
from config.settings import Settings
from entities.s3_bucket import S3Bucket


class MainS3Operations:
    def __init__(self):
        self.s3_session = S3Adapter().create_s3_session()
        self.region = Settings().get_region_name()
        self.location = {'LocationConstraint': self.region}

    def create_bucket(self, bucket_name):
        response = self.s3_session.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration=self.location)
        return response

    def list_buckets(self):
        response = self.s3_session.list_buckets()
        return response

    def upload(self, file_name, file_path, bucket_name):
        response = self.s3_session.upload_file(
            file_path,
            bucket_name,
            file_name
            )
        return response
