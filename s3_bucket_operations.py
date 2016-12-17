#!/usr/bin/python
__author__="Gaurav Khandave"

import boto3
import sys
import botocore

action = sys.argv[1]
bucket_name = sys.argv[2]

s3_client = boto3.client('S3')

if action == 'create-bucket':
    print "Creating bucket"
    s3_client.create_bucket(Bucket=bucket_name)

s3_resource = boto3.resource('S3')

if action == 'delete-bucket':
    print "Deleting bucket"
    # Handling the exception using botocore
    try:
        bucket = s3_resource.Bucket(bucket_name)
        # We need to delete all the objects in bucket first as it doesnt allow us to delete a non-empty bucket directly.
        for key in bucket.objects.all():
            key.delete()
        # After deleting objects in the bucket we can delete bucket
        bucket.delete()
    except botocore.exceptions.ClientError as e:
        print e.response['Error']['Code']

if action == 'upload-object':
    print "Uploading object"
    # To upload the file into bucket, the file needed to be created in
    # amazon environment and then it will be put into the bucket
    s3_resource.Object(bucket_name,"file.txt").put(Body=open('/tmp/file.txt','r'))