### DATA ORCHESTRATION TOOLS COMPARISON PROJECT
## Apache Airflow vs Prefect vs Dagster
# PROJECT OVERVIEW

This project demonstrates and compares three popular data orchestration tools—Apache Airflow, Prefect, and Dagster—by implementing the same ETL (Extract, Transform, Load) pipeline using each tool. The goal is to understand how different orchestration frameworks handle workflow definition, execution, monitoring, and observability while reusing identical business logic.

The ETL pipeline processes a synthetic user activity dataset, performs transformations such as filtering and aggregation, and writes the processed output to a Parquet file. By keeping the ETL logic common across all tools, the comparison focuses purely on orchestration behavior rather than data processing differences.

# PROJECT DIRECTORY STRUCTURE
data-orchestration-comparison/
│
├── airflow/
│   ├── dags/
│   │   └── user_activity_pipeline.py
│
├── prefect/
│   └── flow.py
│
├── dagster/
│   └── job.py
│
├── shared/
│   └── etl_logic.py
│
├── synthetic_events.csv
├── output.parquet
├── COMPARISON.md
└── README.md


→ shared/etl_logic.py contains the common ETL logic reused by all orchestration tools.
→ Each orchestration tool has its own folder but uses the same ETL functions.

# ETL PIPELINE DESCRIPTION

The ETL pipeline consists of the following stages:

→ Extract: Reads user activity data from synthetic_events.csv.
→ Transform: Filters records, performs aggregations, and computes session-based metrics.
→ Load: Writes the transformed data to output.parquet.

This structure ensures consistency across Airflow, Prefect, and Dagster implementations.

# ORCHESTRATION TOOLS IMPLEMENTED
# ➤ Apache Airflow

The Airflow ETL pipeline was implemented using a Directed Acyclic Graph (DAG) where each ETL step is defined as a task using Python operators. Task dependencies were explicitly declared to control execution order. The Airflow scheduler handled task execution, retries, and logging. The Airflow Web UI was used to monitor DAG runs, task states, execution logs, and retries, making it suitable for production-grade and scheduled batch pipelines.

# How to verify Airflow execution
→ Start Airflow services using Docker
→ Open Airflow UI (http://localhost:8080)
→ Trigger the DAG user_activity_pipeline
→ Ensure all tasks turn green (success)

# ➤ Prefect

The Prefect ETL pipeline was implemented using Python-native decorators. Each ETL step was defined as a @task, and orchestration was managed using a @flow. The pipeline reused shared ETL logic without duplication and executed successfully in a local environment without requiring a persistent scheduler or database. Prefect provided automatic logging, retries, and clear task and flow execution states.

# How to verify Prefect execution

The Prefect flow was executed locally and monitored using the Prefect UI.

python prefect/flow.py


After execution, the Prefect UI was accessed at:

http://127.0.0.1:4200/dashboard?flow-run-state=completed


Using the Prefect UI, the following were verified:
→ Successful completion of the flow
→ Task-level execution status
→ Logs and retry behavior
→ Confirmation that output.parquet was generated


→ Successful execution is confirmed when all tasks complete and output.parquet is generated.

# ➤ Dagster

The Dagster ETL pipeline was implemented using an asset-oriented approach, where data assets and their dependencies were explicitly defined. The pipeline reused the same shared ETL logic to ensure consistency with the Airflow and Prefect implementations. Dagster emphasized data lineage, dependency awareness, and observability. The Dagit UI provided clear visualization of assets, execution order, and failure points.

# How to verify Dagster execution

dagster dev


→ Open Dagit UI (http://localhost:3000)
→ Materialize the defined assets
→ Confirm successful asset execution and output generation

# OUTPUT VERIFICATION

After successful execution of any orchestration tool:

→ output.parquet should be created in the project directory
→ The file confirms successful completion of the ETL pipeline
→ The same output is produced regardless of the orchestration tool used

# COMPARISON DOCUMENTATION

A detailed conceptual and project-level comparison is provided in:

COMPARISON.md


This includes:
→ Tool-wise strengths and weaknesses
→ Feature comparison table
→ Project-level observations
→ Final conclusions

# CONCLUSION

This project demonstrates how the same ETL logic can be orchestrated using different tools, highlighting their architectural differences and use cases. Apache Airflow excels in enterprise-scale, scheduled workflows, Prefect offers developer-friendly and flexible execution, and Dagster focuses on data-centric orchestration with strong lineage and observability. The comparison provides practical insight into choosing the right orchestration tool based on project requirements.