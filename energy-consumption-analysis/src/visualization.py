import matplotlib.pyplot as plt
import seaborn as sns
import os
import matplotlib

# Set non-interactive backend to avoid GUI issues in web server
matplotlib.use('Agg')

def check_and_create_dir():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(project_root, "static", "plots")
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

def plot_consumption_over_time(df):
    out_dir = check_and_create_dir()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x='date', y='consumption_mwh', hue='state')
    plt.title("Electricity Consumption Over Time")
    plt.xlabel("Date")
    plt.ylabel("Consumption (MWh)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "electricity_over_time.png"))
    plt.close()

def plot_state_comparison(df):
    out_dir = check_and_create_dir()
    plt.figure(figsize=(8, 5))
    avg_conf = df.groupby('state')['consumption_mwh'].mean().reset_index()
    sns.barplot(data=avg_conf, x='state', y='consumption_mwh')
    plt.title("State-wise Average Consumption")
    plt.xlabel("State")
    plt.ylabel("Average Consumption (MWh)")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "state_consumption.png"))
    plt.close()

def plot_monthly_trend(df):
    out_dir = check_and_create_dir()
    df_temp = df.copy()
    df_temp['month'] = df_temp['date'].dt.to_period('M').astype(str)
    monthly_data = df_temp.groupby('month')['consumption_mwh'].sum().reset_index()
    
    plt.figure(figsize=(8, 5))
    sns.barplot(data=monthly_data, x='month', y='consumption_mwh')
    plt.title("Monthly Energy Consumption Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Consumption (MWh)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "monthly_trend.png"))
    plt.close()

def plot_peak_load(df):
    out_dir = check_and_create_dir()
    plt.figure(figsize=(10, 5))
    
    daily_data = df.groupby('date')['consumption_mwh'].sum().reset_index()
    peak_idx = daily_data['consumption_mwh'].idxmax()
    peak_day = daily_data.loc[peak_idx]
    
    sns.lineplot(data=daily_data, x='date', y='consumption_mwh', color='blue', label='Daily Total')
    plt.scatter(peak_day['date'], peak_day['consumption_mwh'], color='red', s=100, zorder=5, label='Peak Load')
    plt.title("Peak Load Period Analysis")
    plt.xlabel("Date")
    plt.ylabel("Total Consumption (MWh)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "peak_load.png"))
    plt.close()

def plot_anomalies(df_with_anomalies):
    out_dir = check_and_create_dir()
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=df_with_anomalies, x='date', y='consumption_mwh', 
                    hue='is_anomaly', palette={False: 'blue', True: 'red'})
    plt.title("Anomaly Detection (Abnormal Spikes)")
    plt.xlabel("Date")
    plt.ylabel("Consumption (MWh)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "anomalies.png"))
    plt.close()

def generate_all_plots(df, df_anomalies):
    plot_consumption_over_time(df)
    plot_state_comparison(df)
    plot_monthly_trend(df)
    plot_peak_load(df)
    plot_anomalies(df_anomalies)
    print("[Visualization] Generated all plots successfully.")
