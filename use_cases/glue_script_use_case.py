class GlueScriptUseCase:
    def __init__(self, s3_adapter, glue_script_entity):
        self.s3_adapter = s3_adapter
        self.glue_script_entity = glue_script_entity

    def upload_script(self, bucket_name):
        self.s3_adapter.upload_file(
            bucket_name,
            self.glue_script_entity.script_location
            )
