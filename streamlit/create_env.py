from pathlib import Path

def create_env_file(path: str = ".env"):
    """
    Creates a .env file
    """
    env_path = Path(path)

    if env_path.exists():
        print(f"{env_path} already exists. Skipping creation.")
        return

    content = """# AWS Credentials
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=your-aws-region

# S3 Configuration
S3_BUCKET_NAME=project-s3-bucket

# # Redshift Configuration
# REDSHIFT_CLUSTER_ID=your-cluster
# REDSHIFT_DATABASE=your-db
# REDSHIFT_DB_NAMESPACE=your-namespace
# REDSHIFT_DB_USER=redshift-user
# REDSHIFT_DB_PASSWORD=redshift-password

# Data Configuration
DATA_FILE_PATH=s3_data/flights/flights.csv

# Simulation Settings
NUM_CHUNKS=4
UPLOAD_INTERVAL=10"""
    env_path.write_text(content, encoding="utf-8")
    print(f"Created env file at {env_path}")

