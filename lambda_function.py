import uuid

import boto3
import os

# Get the service client.
s3 = boto3.client('s3')
   
def lambda_handler(event, context):

   # Generate a random S3 key name
   upload_key = uuid.uuid4().hex

   # Generate the presigned URL for put requests
   presigned_url = s3.generate_presigned_url(
       ClientMethod='put_object',
       ExpiresIn=60,
       Params={
           'Bucket': os.environ["bucketName"],
           'Key': upload_key
       }
   )

   # Return the presigned URL
   return {
       "upload_url": presigned_url
   }