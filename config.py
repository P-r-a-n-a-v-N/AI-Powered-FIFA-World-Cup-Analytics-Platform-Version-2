import os

class Settings:
    aws_region: str = os.getenv('AWS_REGION', 'ap-south-1')
    s3_bucket: str = os.getenv('S3_BUCKET', 'fifa-worldcup-data')
    athena_workgroup: str = os.getenv('ATHENA_WORKGROUP', 'fifa_analytics')
    athena_database: str = os.getenv('ATHENA_DATABASE', 'fifa_worldcup_db')
    quicksight_namespace: str = os.getenv('QUICKSIGHT_NAMESPACE', 'default')
    bedrock_region: str = os.getenv('BEDROCK_REGION', 'us-east-1')

settings = Settings()
