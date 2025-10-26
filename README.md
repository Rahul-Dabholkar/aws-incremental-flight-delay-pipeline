# AWS Incremental Flight Delay Analysis Pipeline

This project implements an automated ETL pipeline for processing and analyzing flight delay data using various AWS services. The pipeline is designed to handle incremental data loads efficiently and provide insights through Redshift analytics. A Streamlit dashboard is also made to simulate incremental data load to S3 and analyse fight delays using Plotly.

## Project Structure

```
aws-incremental-etl-flight-analysis/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── architecture/            # Architecture diagrams
├── glue_jobs/              # AWS Glue ETL jobs
├── eventbridge/            # EventBridge scheduling
├── step_functions/         # Step Functions workflow
├── sql/                    # SQL scripts for Redshift
├── s3_data/               # Sample data files
├── notebooks/             # Analysis notebooks
└── docs/                  # Detailed documentation
```

## Documentation

Detailed documentation is available in the `docs/` directory:
- Project Overview: `docs/project_overview.md`
- AWS Services Used: `docs/aws_services_used.md`
- Architecture and Pipeline: `docs/architecture/high-level-overview.png`, `docs/architecture/step-functions-pipeline.png`


## Features

- Incremental data loading from S3
- Automated ETL using AWS Glue
- Orchestration using Step Functions
- Scheduled execution via EventBridge
- Data warehousing in Redshift
- Analytics using Jupyter notebooks

## Prerequisites

- AWS Account with appropriate permissions
- Python 3.8+
- AWS CLI configured
- Access to AWS services: S3, Glue, Step Functions, EventBridge, Redshift

## Setup and Installation

1. Clone the repository
2. Install UV `pip install uv`
3. Create VirEnv `uv venv`
4. Activate VirEnv `.\.venv\Scripts\activate`
5. Install dependencies: `uv pip install -r requirements.txt`
6. Run setup script `python .\streamlit\setup.py`. This creates .env file and download data from Kaggle
7. Configure AWS credentials
8. Deploy AWS resources using provided scripts\
9. Simulate using Streamlit `streamlit run .\streamlit\dashboard.py`

