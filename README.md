# AWS Data Pipeline Project

This project provides a solution to manage a data pipeline from an AWS SQL Server RDS to Snowflake using AWS Glue, with intermediate storage in S3. The project is structured based on Clean Architecture principles, ensuring separation of concerns and modularity.

## Project Structure

- `main.py`: Entry point for the application.
- `config`: Contains settings and configurations for RDS, S3, and Snowflake.
- `entities`: Defines primary business entities for RDS, S3, and Snowflake.
- `use_cases`: Contains business rules and use cases for RDS, S3, and Snowflake operations.
- `interface_adapters`: Implements operations for RDS, S3, and Snowflake using appropriate clients or connectors.
- `frameworks_and_drivers`: High level operations and AWS session management.

## Setup

1. Install the required Python packages:

2. Update the `config/settings.py` with your AWS and Snowflake credentials and configurations.

## Usage

### RDS Operations

```python
from frameworks_and_drivers.main_db_operations import create_rds_instance, delete_rds_instance

# Create RDS instance
create_rds_instance()

# Delete RDS instance
delete_rds_instance(instance_id="your_instance_id")

# S3 Operations
from frameworks_and_drivers.main_s3_operations import create_s3_bucket, delete_s3_bucket, list_s3_objects

# Create S3 bucket
create_s3_bucket()

# List objects in S3 bucket
objects = list_s3_objects()
print(objects)

# Delete S3 bucket
delete_s3_bucket()

# Snowflake Operations
from frameworks_and_drivers.main_snowflake_operations import execute_snowflake_query

# Execute Snowflake query
results = execute_snowflake_query("SELECT * FROM your_table")
print(results)
