#!/usr/bin/python
import boto
import sys
import boto.sqs
import json
import time
import os
import pprint
#Usage 
#./restoreobject bucket_name
s3 = boto.connect_s3()
bucket_name = sys.argv[1]

if not s3.lookup(bucket_name):
        print "Bucket did not exist.. Creating bucket... Bucket created"
        s3.create_bucket(bucket_name)

bucket_name = s3.get_bucket(bucket_name)

sqs = boto.sqs.connect_to_region("us-east-1")
queue = sqs.get_queue('sqs_queue_name')
from boto.sqs.message import RawMessage
queue.set_message_class(RawMessage)
result = queue.get_messages()

if len(result) == 0:
        print "There are not messages available."
        exit(1)
#read the message body
m = result[0]
body = m.get_body()
decoded_message = json.loads(body)
decoded_message = json.loads(decoded_message["Message"])


print decoded_message["Key"]

queue.delete_message(m)

#apply the black filter to the image
os.system("convert images/"+decoded_message["Key"] + " -monochrome " + decoded_message["Key"])
#upload the image back to the location it was before it was lost
from boto.s3.key import Key
key = Key(bucket_name)
key.key = decoded_message["Key"]
key.set_contents_from_filename(decoded_message["Key"])
print "Your file has been automatically recreated and uploaded to its proper location"