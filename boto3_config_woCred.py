#!/usr/bin/python
__author__="Gaurav Khandave"

# This example creates a bucket on s3 service on aws console using boto3 with credentials.
# Credentials are not required as the user is assigned with admin role to an EC2 instance.
import boto3

s3 = boto3.resource("s3")

s3.create_bucket(Bucket="myFirstUniqueBucket")