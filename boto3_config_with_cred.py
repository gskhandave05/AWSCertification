#!/usr/bin/python
__author__="Gaurav Khandave"

# This example creates a bucket on s3 service on aws console using boto3 with credentials.
# Credentials are required when user is not assigned admin role to an EC2 instance i.e. user is outside aws environment.
from boto3.session import Session

session = Session(aws_access_key_id="Your access key id goes here",aws_secret_access_key="Your secret access key goes here")

s3=session.resource('S3')

s3.create_bucket(Bucket="myUniqueBucket")