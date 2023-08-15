from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)


class Ec2Adapter:
    def __init__(self, aws_session):
        self.ec2 = aws_session.client('ec2')

    def create_security_group(self, group_name, description, vpc_id):
        try:
            response = self.ec2.create_security_group(
                GroupName=group_name,
                Description=description,
                VpcId=vpc_id
            )
            logger.info(f"Security Group {group_name} created.")
            return response['GroupId']
        except ClientError as e:
            logger.error(e)
            raise e

    def authorize_security_group_ingress(self,
                                         group_id,
                                         ip_protocol,
                                         from_port,
                                         to_port,
                                         cidr_ip
                                         ):
        try:
            response = self.ec2.authorize_security_group_ingress(
                GroupId=group_id,
                IpPermissions=[
                    {
                        'IpProtocol': ip_protocol,
                        'FromPort': from_port,
                        'ToPort': to_port,
                        'IpRanges': [
                            {
                                'CidrIp': cidr_ip,
                                'Description': 'SSH access from the Internet'
                            },
                        ],
                    },
                ],
            )
            logger.info(f"Ingress Successfully Set {response}")
        except ClientError as e:
            logger.error(e)
            raise e
