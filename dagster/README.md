## Dagster ETL Pipeline Implementation

This directory contains the Dagster implementation of the ETL pipeline, focusing on asset-based design, strong typing, and explicit data dependencies. The pipeline is defined using Dagster jobs and ops, enabling excellent observability and maintainability.

# Directory Structure

The Dagster implementation emphasizes clarity and modularity.

repository.py defines the Dagster repository

jobs/etl_job.py defines the ETL job and op dependencies

etl/transformations.py contains transformation logic

Dockerfile builds the Dagster execution environment

workspace.yaml configures the Dagster workspace

# README.md documents execution steps

# Setup Instructions

Ensure Docker is installed.

Navigate to the Dagster directory.

cd dagster


Build the Docker image.

docker build -t dagster-etl .

# Running the Pipeline

The Dagster job is executed using the Dagster CLI with configurable run parameters.

Example execution:

docker run --rm \
  -v $(pwd)/../data:/data \
  -v $(pwd)/../output:/output \
  dagster-etl \
  dagster job execute \
  -f jobs/etl_job.py \
  -c run_config.yaml


The run configuration specifies input and output paths, enabling parameterization.

# Retry Logic Implementation

Retry behavior is implemented at the op level using Dagster’s retry policy. This ensures that only the failing computation is retried, not the entire pipeline, improving efficiency and reliability.

# Backfill Execution

Dagster supports backfills through repeated job execution with varying run configurations. Because the pipeline is deterministic and parameter-driven, historical data processing is fully supported.

# Output Validation

The Parquet output produced by Dagster matches exactly with the outputs from the Airflow and Prefect pipelines when run with identical inputs and parameters.

# Design Notes

This implementation demonstrates Dagster’s strengths in explicit data modeling, clear lineage tracking, and strong separation between computation and orchestration.