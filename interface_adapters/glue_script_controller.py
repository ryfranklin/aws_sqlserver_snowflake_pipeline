class GlueScriptController:
    def __init__(self, s3_adapter):
        self.s3_adapter = s3_adapter

    def run(self):
        self.glue_script.run()
