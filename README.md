# AWS Disaster Recovery Architecture with Secure Backup and Recovery

## Project Overview

This project demonstrates a foundational AWS disaster recovery setup for a healthcare technology application. It focuses on secure application hosting, backup storage, and application recovery using AWS services.

The primary environment is deployed in the Asia Pacific (Sydney) region (`ap-southeast-2`).

## Architecture

The implemented architecture includes:

- Amazon VPC for network isolation.
- Public and private subnets.
- Internet Gateway and route tables.
- Amazon EC2 hosting a Python Flask application.
- IAM role with restricted Amazon S3 permissions.
- Amazon S3 for application backup storage.
- S3 Versioning and Server-Side Encryption (SSE-S3).

## AWS Services Used

| Service | Purpose |
|---|---|
| Amazon VPC | Network isolation |
| Amazon EC2 | Application hosting |
| Amazon S3 | Backup storage |
| AWS IAM | Access control |
| Internet Gateway | Internet connectivity |
| Security Groups | Network traffic control |

## Implementation Details

### 1. Network Infrastructure

- Created a custom VPC named `DR-Primary-VPC`.
- Configured public and private subnets across two Availability Zones.
- Configured an Internet Gateway and route tables.
- Created separate security groups for the web server and prepared database layer.

### 2. Application Deployment

- Launched an Amazon Linux 2023 EC2 instance (`t3.micro`).
- Deployed a Python Flask application.
- Verified application accessibility through a web browser.

### 3. IAM Configuration

- Created an EC2 IAM role named `DR-EC2-S3-Access-Role`.
- Configured a custom policy named `DR-S3-Backup-Policy`.
- Granted only the required S3 bucket listing, upload, and download permissions.

### 4. S3 Backup Configuration

- Created an S3 bucket for application backups.
- Enabled S3 Versioning.
- Enabled Block Public Access.
- Configured default encryption using SSE-S3.
- Uploaded the application backup ZIP file.

### 5. Backup Recovery Test

The recovery process was successfully tested:

- Downloaded the application ZIP backup from S3.
- Extracted the backup into a separate recovery directory.
- Created a Python virtual environment.
- Installed application dependencies.
- Checked Python syntax.
- Started the recovered Flask application on port `5001`.
- Verified the application response using `curl`.

**Recovery test result:** Successful. The restored application returned the expected HTML response.

## Security Measures

- IAM role-based access instead of hardcoded AWS credentials.
- Restricted S3 permissions.
- S3 Block Public Access enabled.
- S3 Versioning enabled.
- SSE-S3 encryption enabled.
- Security groups configured to restrict network access.

## Disaster Recovery Scope and Limitations

The current implementation demonstrates application backup and recovery within the same AWS region.

The original design also considered:

- S3 Cross-Region Replication.
- Amazon RDS and cross-region read replicas.
- Secondary-region EC2 deployment.
- DNS-based failover using Amazon Route 53.
- Automated disaster recovery.

These components were not implemented because the current AWS account has access restricted to the Sydney region. They remain planned enhancements.

No actual cross-region failover or automated failover was performed.

## Recovery Objectives

- **RPO:** Not formally measured. The backup frequency and potential data-loss window need to be defined.
- **RTO:** Not formally measured. The successful recovery test confirms application restoration, but the complete recovery duration was not timed.

## Key Learnings

- AWS networking and VPC configuration.
- EC2 application deployment.
- IAM roles and least-privilege permissions.
- S3 backup storage and versioning.
- Server-side encryption.
- Application backup and restoration.
- Recovery validation and troubleshooting.

## Future Improvements

- Implement cross-region backup replication when eligible.
- Integrate Amazon RDS.
- Configure a secondary recovery environment.
- Implement DNS-based failover.
- Automate backup and recovery workflows.
- Measure and validate RTO and RPO.

## Project Status

**Primary infrastructure and application backup/recovery demonstration completed. Cross-region disaster recovery remains planned.**

**Region:** Asia Pacific (Sydney) — `ap-southeast-2`
