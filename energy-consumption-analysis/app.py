from flask import Flask, render_template
from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.anomaly_detection import detect_anomalies
from src.visualization import generate_all_plots
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Load and process data
    df = load_data()
    df_clean = preprocess_data(df)

    # Run anomaly detection
    df_anomalies = detect_anomalies(df_clean)

    # Generate all plots
    generate_all_plots(df_clean, df_anomalies)

    # Compute metrics for key stats cards
    total_consumption = df_clean['consumption_mwh'].sum()
    daily_totals = df_clean.groupby('date')['consumption_mwh'].sum()
    avg_daily_consumption = daily_totals.mean()
    peak_load = daily_totals.max()
    num_anomalies = int(df_anomalies['is_anomaly'].sum())

    # Dataset preview (first 5 rows)
    preview_df = df_clean.head(5).copy()
    preview_df['date'] = preview_df['date'].dt.strftime('%Y-%m-%d')
    preview_data = preview_df.to_dict('records')

    return render_template('home.html',
                           total_consumption=total_consumption,
                           avg_daily=avg_daily_consumption,
                           peak_load=peak_load,
                           num_anomalies=num_anomalies,
                           preview_data=preview_data)

@app.route('/dashboard')
def dashboard():
    # Load and process data
    df = load_data()
    df_clean = preprocess_data(df)
    
    # Run anomaly detection
    df_anomalies = detect_anomalies(df_clean)
    
    # Generate all plots
    generate_all_plots(df_clean, df_anomalies)
    
    # Compute metrics for overview
    total_consumption = df_clean['consumption_mwh'].sum()
    
    daily_totals = df_clean.groupby('date')['consumption_mwh'].sum()
    avg_daily_consumption = daily_totals.mean()
    peak_load = daily_totals.max()
    
    num_anomalies = int(df_anomalies['is_anomaly'].sum())
    
    # Dataset Preview (first 5 rows)
    preview_df = df_clean.head(5).copy()
    preview_df['date'] = preview_df['date'].dt.strftime('%Y-%m-%d')
    preview_data = preview_df.to_dict('records')
    
    # Render HTML dashboard
    return render_template('dashboard.html', 
                           total_consumption=total_consumption,
                           avg_daily=avg_daily_consumption,
                           peak_load=peak_load,
                           num_anomalies=num_anomalies,
                           preview_data=preview_data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
