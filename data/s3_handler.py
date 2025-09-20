import boto3
import os

def get_s3_client():
    """Create an S3 client using credentials from environment variables."""
    s3 = boto3.client(
        's3',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    return s3

def upload_file_to_s3(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket."""
    if object_name is None:
        object_name = os.path.basename(file_name)
    
    s3 = get_s3_client()
    s3.upload_file(file_name, bucket, object_name)

def download_file_from_s3(bucket, object_name, file_name):
    """Download a file from an S3 bucket."""
    s3 = get_s3_client()
    s3.download_file(bucket, object_name, file_name)

def list_files_in_s3(bucket, prefix=''):
    """List files in a specific S3 bucket."""
    s3 = get_s3_client()
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    if 'Contents' in response:
        return [obj['Key'] for obj in response['Contents']]
    return []