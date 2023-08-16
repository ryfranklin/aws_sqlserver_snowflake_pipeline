import boto3


class GlueAdapter:
    def __init__(self):
        self.glue_client = boto3.client('glue')

    def create_job(self, script_location, job_name):
        # The method that sets up and starts the AWS Glue Job
        role = ""

        response = self.glue_client.create_job(
            Name=job_name,
            Role=role,
            Command={
                'Name': 'glueetl',
                'ScriptLocation': script_location
            },
            DefaultArguments={
                '--job-language': 'python',
            }
        )
        return response

    def start_job(self, job_name):
        response = self.glue_client.start_job_run(JobName=job_name)
        return response
