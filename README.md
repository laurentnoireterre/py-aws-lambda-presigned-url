# Description

Simple python program to generate a S3 presigned url.

# Packaging

Clone the repository and zip its content
```
cd py-aws-lambda-presigned-url
zip -r ../py-aws-lambda-presigned-url.zip .
```

# Installation & Usage 

Connect to AWS console and create a Lambda having this properties:
   - Runtime: `Python 3.6`
   - Role:
```
Allow: logs:CreateLogGroup
Allow: logs:CreateLogStream
Allow: logs:PutLogEvents
Allow: s3:*

Resource: *
```
   - Environment variables: 
     - Add an environment variable named `bucketName` and containing the S3 bucket name used to generate the presigned url

Deploy the function code by uploading the zip package.
