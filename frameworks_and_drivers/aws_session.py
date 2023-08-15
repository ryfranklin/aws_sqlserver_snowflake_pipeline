import boto3
from config.settings import Settings


class AwsSession:
    """
    Helper class to manage AWS boto3 sessions.
    """

    def __init__(self):
        """
        Initializes the AwsSession with a specific AWS region.

        Args:
        - region_name (str): The AWS region for the session (e.g.,
            'us-west-2' for Oregon).
        """

        self.region_name = Settings().get_region_name()
        self.access_key = Settings().get_access_key()
        self.secret_key = Settings().get_secret_key()
        self.session = self._create_session()

    def _create_session(self):
        """
        Creates a new boto3 session with the specified region.

        Returns:
        - boto3.Session: A boto3 session object.
        """
        return boto3.session.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region_name,

            )

    def get_aws_session(self):
        """
        Retrieves the boto3 session.

        Returns:
        - boto3.Session: The initialized boto3 session object.
        """
        return self.session

    def verify_aws_sesssion(self):
        try:
            # Create an s3 client using your default session
            s3 = boto3.client('s3')

            # List the buckets
            response = s3.list_buckets()
            return response

        except Exception as e:
            print(f"An error occurred: {e}")
            return False
