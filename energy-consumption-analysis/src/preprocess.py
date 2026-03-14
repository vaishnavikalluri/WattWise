import pandas as pd

def preprocess_data(df):
    """
    Clean dataset, convert date column to datetime format,
    and handle missing values.
    """
    if df is None or df.empty:
        print("[Preprocess] Empty DataFrame received.")
        return df

    df_clean = df.copy()

    # Convert date to datetime format
    if 'date' in df_clean.columns:
        df_clean['date'] = pd.to_datetime(df_clean['date'])

    # Handle missing values using forward fill for time series
    df_clean.ffill(inplace=True)
    df_clean.dropna(inplace=True)

    print(f"[Preprocess] Preprocessing complete. Shape: {df_clean.shape}")
    return df_clean
