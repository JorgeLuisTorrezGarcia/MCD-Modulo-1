import pandas as pd

def load_data(file_path):
    #Load data from a CSV file.
    return pd.read_csv(file_path)

def clean_missing_values(df):
    # replace missing values with the mean of each column.
    return df.fillna(df.mean(numeric_only=True))
