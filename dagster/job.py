from dagster import op, job
import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from shared.etl_logic import extract_data, transform_data, load_data


@op
def extract():
    return extract_data("synthetic_events.csv")


@op
def transform(df):
    return transform_data(df)


@op
def load(df):
    load_data(df, "output.parquet")


@job
def user_activity_dagster_etl():
    load(transform(extract()))
