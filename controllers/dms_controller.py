from use_cases.dms_sqlserver import SetupDMSForRDS
from interface_adapters.dms_sqlserver_adapter import DMSAdapter


class DMSController:

    def __init__(self, aws_session):
        dms_client = aws_session.client('dms')
        self.dms_adapter = DMSAdapter(dms_client)
        self.use_case = SetupDMSForRDS(self.dms_adapter)

    def setup_dms(
            self,
            instance_details,
            source_endpoint_details,
            target_endpoint_details,
            task_details
            ):
        self.use_case.execute(
            instance_details,
            source_endpoint_details,
            target_endpoint_details,
            task_details
            )
