class S3Bucket:
    def __init__(self, name, region, creation_date):
        self.name = name
        self.region = region
        self.creation_date = creation_date


class S3Object:
    def __init__(self, key, last_modified, size):
        self.key = key
        self.last_modified = last_modified
        self.size = size
