#! /usr/local/bin/python3
import boto3
import botocore
from urllib.parse import urlparse
from urllib.parse import urlparse

BUCKET_NAME = 'kammana' # replace with your bucket name
KEY = 'error.html' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
