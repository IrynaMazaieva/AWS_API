from typing import List

import boto3
import os
import uuid


def upload_file(filename: str, bucket: str):
    s3_client = boto3.client('s3')
    object_name = os.path.basename(filename)
    s3_client.upload_file(filename, bucket, object_name)


def download_file(filename: str, bucket: str) -> str:
    s3 = boto3.resource('s3')
    output = f"downloads/{uuid.uuid4()}{filename}"
    s3.Bucket(bucket).download_file(filename, output)
    return output


def list_files(bucket: str) -> List:
    s3 = boto3.client('s3')
    contents = []
    if 'Contents' in s3.list_objects(Bucket=bucket).keys():
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            contents.append(item)
    return contents


def validate_file_type(filename: str, extensions: tuple) -> bool:
    return filename.endswith(extensions)
