from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.analysis import get_peak_load, get_average_consumption, get_monthly_trends, get_daily_trends
from src.anomaly_detection import detect_anomalies
from src.visualization import generate_all_plots

def main():
    print("=== Starting Energy Consumption Analysis ===")
    
    # 1. Load data
    df = load_data()
    if df is None:
        print("Failed to load data. Exiting...")
        return
        
    # 2. Preprocess data
    df_clean = preprocess_data(df)
    
    # 3. Run analysis
    peak_info = get_peak_load(df_clean)
    print("\n[Analysis] Peak Load Info:\n", peak_info['global_peak'])
    
    avg_consumption = get_average_consumption(df_clean)
    print("\n[Analysis] Average Consumption per State:")
    for state, avg in avg_consumption.items():
        print(f"  {state}: {avg:.2f} MWh")
        
    # 4. Run anomaly detection
    df_anomalies = detect_anomalies(df_clean)
    
    # 5. Generate plots
    generate_all_plots(df_clean, df_anomalies)
    
    print("\n=== Analysis Complete ===")
    print("Plots have been saved to the 'static/plots' directory.")

if __name__ == "__main__":
    main()
