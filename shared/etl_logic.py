import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

def transform_data(df):
    df["event_count"] = 1
    return df

def load_data(df, output_path):
    df.to_parquet(output_path, index=False)
