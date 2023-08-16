from entities.dms_sqlserver import (
    ReplicationInstance,
    SourceEndpoint,
    TargetEndpoint,
    ReplicationTask
)


class SetupDMSForRDS:
    """Use Case for setting up DMS from RDS to S3."""

    def __init__(self, dms_adapter):
        self.dms_adapter = dms_adapter

    def execute(self,
                instance_details,
                source_endpoint_details,
                target_endpoint_details,
                task_details
                ):
        # Create replication instance
        rep_instance = ReplicationInstance(**instance_details)
        self.dms_adapter.create_replication_instance(rep_instance)

        # Create source endpoint
        source_endpoint = SourceEndpoint(**source_endpoint_details)
        self.dms_adapter.create_source_endpoint(source_endpoint)

        # Create target endpoint
        target_endpoint = TargetEndpoint(**target_endpoint_details)
        self.dms_adapter.create_target_endpoint(target_endpoint)

        # Create replication task
        rep_task = ReplicationTask(
            source_endpoint,
            target_endpoint,
            **task_details
            )
        self.dms_adapter.create_replication_task(rep_task)
