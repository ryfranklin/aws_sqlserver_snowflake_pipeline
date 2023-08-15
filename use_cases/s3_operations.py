class CreateBucket:
    def execute(self, s3_adapter, bucket_name):
        return s3_adapter.create_bucket(bucket_name)


class ListBuckets:
    def execute(self, s3_adapter):
        return s3_adapter.list_buckets()


class UploadObject:
    def execute(self, s3_adapter, bucket_name, file_name, object_name=None):
        return s3_adapter.upload_object(bucket_name, file_name, object_name)
