# AWS Learnings

Hands-on AWS scripts built while learning core AWS data engineering services — **S3, Lambda, IAM, and Glue** — through small, practical automation examples rather than just theory.

This repo is part of my transition toward Data Engineering / AI-ML Data Engineering roles, alongside my [dbt-snapshot-learnings](https://github.com/meetaghera/dbt-snapshot-learnings) repo (Snowflake + dbt).

## What's in here

### `s3.py`
A local script (run from VS Code) that connects to AWS using `boto3` and IAM credentials loaded from a `.env` file. Used to manage S3 buckets directly — listing buckets and deleting empty ones. This was my starting point for understanding how IAM access keys authenticate `boto3` calls before moving logic into Lambda.

### `mylambda.py`
An AWS Lambda function that automates moving a file inside an S3 bucket:
1. Copies a file from a source key/folder to a destination key/folder
2. Deletes the original file once the copy succeeds

Uses the IAM role attached to the Lambda function itself for permissions — no hardcoded credentials needed, unlike the local `s3.py` script.

### `triggers.py`
A second Lambda function that starts an **AWS Glue** job (`Pipeline1`) using `boto3`, and returns the Glue job run ID. This is designed to run after a file lands in its destination, kicking off downstream processing.

## How the pieces fit together

```
File uploaded to S3 (trigger/ folder)
        │
        ▼
  mylambda.py  →  moves file to destination/ folder
        │
        ▼
  triggers.py  →  starts Glue job (Pipeline1)
```

This mirrors a simple event-driven ETL pattern: **landing zone → file move → pipeline trigger**, similar to patterns used in real production data pipelines.

## AWS services covered
- **S3** — object storage, bucket operations, copy/delete
- **Lambda** — serverless compute, event-driven automation
- **IAM** — roles and permissions for Lambda, access keys for local scripts
- **Glue** — triggering ETL job runs programmatically

## Notes
- Bucket names, region, and Glue job names in these scripts are specific to my test AWS environment and would need to be parameterized for reuse.
- `.env` file (containing AWS credentials) is excluded via `.gitignore` and never committed.

## Why this repo exists
Built as part of a structured AWS learning path (IAM → S3 → Lambda → Glue → Athena → Step Functions), with a project-first approach working toward the **AWS Certified Data Engineer – Associate** certification.
