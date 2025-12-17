from prefect import flow, task
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from shared.etl_logic import extract_data, transform_data, load_data

@task
def extract():
    return extract_data("synthetic_events.csv")

@task
def transform(df):
    return transform_data(df)

@task
def load(df):
    load_data(df, "output.parquet")

@flow(name="user-activity-prefect-etl")
def prefect_etl_flow():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    prefect_etl_flow()
