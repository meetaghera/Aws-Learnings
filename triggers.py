import json
import boto3

def lambda_handler(event, context):
    
    glue_client = boto3.client('glue')

    response = glue_client.start_job_run(JobName='Pipeline1')

    return {
        'statusCode': 200,
        'body': json.dumps(f"Job triggered. Run ID: {response['JobRunId']}")
    }
