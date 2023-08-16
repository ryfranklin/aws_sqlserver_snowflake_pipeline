class DMSSqlServerAdapter:
    """
    Adapter for interfacing with AWS DMS services.
    """

    def __init__(self, dms_client):
        self.dms_client = dms_client

    def create_replication_instance(self, rep_instance_entity):
        ...

    def create_source_endpoint(self, source_endpoint_entity):
        ...

    def create_target_endpoint(self, target_endpoint_entity):
        ...

    def create_replication_task(self, rep_task_entity):
        ...
