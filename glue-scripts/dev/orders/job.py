import sys
from awsglue.utils import getResolvedOptions
import json
import boto3

args = getResolvedOptions(
    sys.argv,
    ['env', 'job_type', 'config']
)

print("===== ORDERS JOB =====")
print("ENV:", args['env'])
print("TYPE:", args['job_type'])
print("CONFIG:", args['config'])

print("Processing only NEW / UPDATED orders...")



config_path = args['config']

# Parse S3 path
# s3://bucket/key
bucket = config_path.replace("s3://", "").split("/")[0]
key = "/".join(config_path.replace("s3://", "").split("/")[1:])

# Read JSON from S3
s3 = boto3.client("s3")
response = s3.get_object(Bucket=bucket, Key=key)
config = json.loads(response["Body"].read().decode("utf-8"))

primary_key = config["primary_key"]
watermark_column = config["watermark_column"]
target_table = config["target_table"]

print("Primary Key:", primary_key)
print("Watermark Column:", watermark_column)
print("Target Table:", target_table)
