import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    """
    Use IsolationForest from scikit-learn to detect abnormal
    spikes in electricity consumption.
    """
    if df is None or df.empty:
        return df

    df_anom = df.copy()
    
    # We train the isolation forest on consumption data
    model = IsolationForest(contamination=0.05, random_state=42)
    X = df_anom[['consumption_mwh']]
    
    df_anom['anomaly'] = model.fit_predict(X)
    
    # -1 implies anomaly, 1 implies normal. Map to boolean for easier plotting
    df_anom['is_anomaly'] = df_anom['anomaly'] == -1
    
    anomalies_count = df_anom['is_anomaly'].sum()
    print(f"[AnomalyDetection] Detected {anomalies_count} anomalies.")
    
    return df_anom
