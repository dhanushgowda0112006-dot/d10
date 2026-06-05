import pandas as pd


def load_data(file):
    df = pd.read_csv(file)
    return df


def basic_info(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": df.isnull().sum().sum()
    }


def numeric_summary(df):
    return df.describe()


def top_players(df):
    
    string_cols = df.select_dtypes(include="object").columns

    if len(string_cols) > 0:
        col = string_cols[0]
        return df[col].value_counts().head(10)

    return None


def correlation(df):
    numeric_df = df.select_dtypes(include='number')

    if len(numeric_df.columns) > 1:
        return numeric_df.corr()

    return None
