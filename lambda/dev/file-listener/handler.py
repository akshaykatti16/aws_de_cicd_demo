import boto3
import os

glue = boto3.client("glue")

def lambda_handler(event, context):
    print("Event:", event)

    response = glue.start_job_run(
        JobName=os.environ["GLUE_JOB_NAME"]
    )

    return {
        "status": "started",
        "jobRunId": response["JobRunId"]
    }
