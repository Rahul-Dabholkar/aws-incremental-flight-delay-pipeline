-- Load data from S3 to Redshift using COPY command
COPY project1_airlines.airports_dim
FROM 's3://project1-airlines-data-ingestion-landing-zone/dim/airports.csv'
IAM_ROLE 'arn:aws:iam::<role-id>:role/redshift_access_s3_role'
DELIMITER ','
IGNOREHEADER 1
REGION 'ap-south-1';
