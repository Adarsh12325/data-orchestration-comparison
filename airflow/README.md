## Apache Airflow ETL Pipeline Implementation

This directory contains the Apache Airflow implementation of the parameterized ETL (Extract, Transform, Load) pipeline built using a Directed Acyclic Graph (DAG). The pipeline reads a synthetic CSV dataset, performs deterministic transformations, and writes the output as a Parquet file. This implementation focuses on production-grade scheduling, retry handling, backfilling, and parameterized execution using Airflow best practices.

# Directory Structure

This folder is organized to clearly separate orchestration logic, business logic, and deployment configuration.

dags/etl_pipeline.py defines the Airflow DAG and task dependencies

etl/transformations.py contains reusable business logic for data transformation

docker-compose.yaml provisions Airflow with a PostgreSQL metadata database

Dockerfile builds a custom Airflow image with required dependencies

requirements.txt lists Python dependencies

# README.md documents setup, execution, and validation steps

# Setup Instructions

Ensure Docker and Docker Compose are installed on your system.

First, navigate to the Airflow directory.

cd airflow


Initialize Airflow metadata and start all services.

docker compose up airflow-init
docker compose up -d


Once services start successfully, access the Airflow web interface at:

http://localhost:8080


Login credentials:

Username: admin

Password: given in the output

# Running the Pipeline

The DAG is named synthetic_etl_airflow. By default, it processes the dataset located at /data/synthetic_events.csv and writes output to /output/airflow_output.parquet.

The pipeline supports runtime parameterization using Airflow’s DAG Run configuration.

Example custom run configuration:

{
  "input_path": "/data/synthetic_events.csv",
  "output_path": "/output/custom_airflow_output.parquet"
}


Trigger the DAG manually from the Airflow UI using “Trigger DAG with config”.

# Retry Logic Implementation

Retry logic is implemented at the task level using Airflow’s native configuration. The transformation task is configured with multiple retries and a retry delay to handle transient failures reliably. This ensures robustness without polluting business logic with orchestration concerns.

# Backfill Execution

Backfilling is supported using Airflow’s CLI or UI. The DAG is defined with a logical start_date and no catchup disabled, allowing historical runs.

CLI example:

docker exec -it airflow-webserver airflow dags backfill synthetic_etl_airflow \
  -s 2024-01-01 -e 2024-01-05

# Output Validation

The final output is written as a Parquet file. When run with identical parameters and input data, this output is guaranteed to be byte-identical to the outputs produced by the Prefect and Dagster implementations.

# Design Notes

This Airflow implementation follows best practices by clearly separating transformation logic from orchestration code, using parameterized execution, supporting backfills, and relying on Airflow’s scheduler for reliability and observability.