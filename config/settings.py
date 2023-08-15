import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()

    def get_region_name(self):
        return os.getenv('AWS_REGION')

    def get_sql_server_config(self):
        return {
            "DBInstanceIdentifier": os.getenv(
                'RDS_SQLSERVER_DB_INSTANCE_IDENTIFIER'
                ),
            "MasterUsername": os.getenv('RDS_SQLSERVER_MASTER_USERNAME'),
            "MasterUserPassword": os.getenv('RDS_SQLSERVER_MASTER_PASSWORD'),
            "Engine": os.getenv('RDS_SQLSERVER_ENGINE'),
            "DBInstanceClass": os.getenv('RDS_SQLSERVER_INSTANCE_CLASS'),
            "AllocatedStorage": int(
                os.getenv('RDS_SQLSERVER_ALLOCATED_STORAGE')
                ),
            "BackupRetentionPeriod": int(
                os.getenv('RDS_SQLSEVER_BACKUP_RETENTION_PERIOD')
                ),
            "StorageType": os.getenv('RDS_SQLSERVER_STORAGE_TYPE'),
            "PubliclyAccessible": bool(
                os.getenv('RDS_SQLSERVER_PUBLICLY_ACCESSIBLE')
                ),
            "LicenseModel": os.getenv('RDS_SQLSERVER_LICENSE_MODEL'),
        }

    def get_access_key(self):
        return os.getenv('AWS_ACCESS_KEY_ID')

    def get_secret_key(self):
        return os.getenv('AWS_SECRET_ACCESS_KEY')
