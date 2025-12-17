from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from shared.etl_logic import extract_data, transform_data, load_data

def extract():
    return extract_data()

def transform(**context):
    df = context["ti"].xcom_pull(task_ids="extract_task")
    return transform_data(df, ["US"])

def load(**context):
    df = context["ti"].xcom_pull(task_ids="transform_task")
    load_data(df, "/opt/project/output.parquet")

default_args = {
    "retries": 2,
    "retry_delay": timedelta(seconds=10),
}

with DAG(
    dag_id="user_activity_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load,
    )

    extract_task >> transform_task >> load_task
