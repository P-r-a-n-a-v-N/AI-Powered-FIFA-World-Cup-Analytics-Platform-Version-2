import boto3
from .config import settings

_session = boto3.Session(region_name=settings.aws_region)

s3 = _session.client('s3')
athena = _session.client('athena')
quicksight = _session.client('quicksight')

bedrock = boto3.client('bedrock-runtime', region_name=settings.bedrock_region)
