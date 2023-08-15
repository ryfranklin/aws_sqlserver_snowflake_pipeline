from use_cases.s3_operations import CreateBucket, UploadObject


class S3Controller:
    def __init__(self, s3_adapter):
        self.s3_adapter = s3_adapter

    def create_and_upload(self, bucket_name, file_name):
        CreateBucket().execute(self.s3_adapter, bucket_name)
        UploadObject().execute(self.s3_adapter, bucket_name, file_name)
