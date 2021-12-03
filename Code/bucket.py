#!/usr/local/bin/python3


# Import the required libraries
import logging
import boto3
from botocore.exceptions import ClientError

# Set the bucket name
bucket_name = 's3-cpd-2021'

# This function attempts to create a bucket with the name 'bucker_name'
# The location is set for 'eu-west-2'
# If the bucket creation fails, ClientError will output an error
def create_bucket(bucket_name, region='eu-west-2'):
    try:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name,
                                CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


# Call the function to create the bucket
create_bucket(bucket_name)
