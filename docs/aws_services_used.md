# AWS Services Used

This document outlines the AWS services used in the flight delay pipeline and their roles.

## Core Services

### Amazon S3
- **Purpose**: Data storage for raw and processed data
- **Usage**:
  - Raw data landing zone
  - Processed data storage
  - Checkpoint files for incremental processing
- **Configuration**:
  - Event notifications for triggering processes

### AWS Glue
- **Purpose**: ETL processing and data catalog
- **Usage**:
  - Data transformation jobs
  - Schema management
- **Components**:
  - Glue Scrapers for Data Scraping
  - Glue Jobs for ETL
  - Glue Catalog for metadata
  - Glue Connections for data sources

### Amazon Redshift
- **Purpose**: Data warehousing and analytics
- **Usage**:
  - Storage of processed data
  - Analytics queries
- **Features**:
  - Columnar storage
  - Distribution keys
  - Sort keys for performance

## Orchestration Services

### AWS Step Functions
- **Purpose**: Workflow orchestration
- **Usage**:
  - Pipeline orchestration
  - Error handling
  - Retry logic
- **Features**:
  - Visual workflow editor
  - Built-in error handling
  - Integration with AWS services

### Amazon EventBridge
- **Purpose**: Scheduling and event management
- **Usage**:
  - Event-based triggers
- **Features**:
  - Event patterns
  - Custom event buses

## Monitoring and Management

### Amazon CloudWatch
- **Purpose**: Monitoring and logging
- **Usage**:
  - Pipeline monitoring
  - Error tracking

### AWS IAM
- **Purpose**: Security and access control
- **Usage**:
  - Service roles
  - Cross-service permissions
  - User access management

## Cost Optimization
- Use of Glue job bookmarks for incremental processing