import boto3
from dotenv import load_dotenv
import os
load_dotenv()

s3 = boto3.client('s3',
                region_name="eu-north-1",
                aws_access_key_id = os.environ ["aws_access_key_id"],
                aws_secret_access_key = os.environ ["aws_secret_access_key"]
)

# List All buckets

#response = s3.list_buckets()
#for bucket in response['Buckets']:
#    print(f'Bucket Name: {bucket["Name"]}, Creation Date: {bucket["CreationDate"]}')

# delete a empty specific bucket
response = s3.delete_bucket(
    Bucket='demo-meet-2026',
    ExpectedBucketOwner='***'
)

