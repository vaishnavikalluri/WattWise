import pandas as pd

def get_peak_load(df):
    """
    Identify peak load periods.
    Returns global peak and peak per state.
    """
    if df is None or df.empty:
        return None

    global_peak_idx = df['consumption_mwh'].idxmax()
    global_peak = df.loc[global_peak_idx]

    peak_per_state = df.loc[df.groupby('state')['consumption_mwh'].idxmax()]

    return {
        'global_peak': global_peak.to_dict(),
        'peak_per_state': peak_per_state.to_dict('records')
    }

def get_average_consumption(df):
    """
    Calculate average consumption per region/state.
    """
    if df is None or df.empty:
        return None
    return df.groupby('state')['consumption_mwh'].mean().to_dict()

def get_monthly_trends(df):
    """
    Identify monthly consumption patterns.
    """
    if df is None or df.empty:
        return None
    df_monthly = df.copy()
    df_monthly['month'] = df_monthly['date'].dt.to_period('M')
    monthly_trend = df_monthly.groupby('month')['consumption_mwh'].sum().reset_index()
    monthly_trend['month'] = monthly_trend['month'].astype(str)
    return monthly_trend

def get_daily_trends(df):
    """
    Identify daily consumption patterns.
    """
    if df is None or df.empty:
        return None
    daily_trend = df.groupby('date')['consumption_mwh'].sum().reset_index()
    daily_trend['date'] = daily_trend['date'].dt.strftime('%Y-%m-%d')
    return daily_trend
