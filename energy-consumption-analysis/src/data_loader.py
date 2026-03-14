import pandas as pd
import os

def load_data(filepath="data/dataset.csv"):
    """
    Load dataset from CSV file using pandas.
    """
    # handle relative path by resolving to project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(project_root, filepath)
    
    try:
        df = pd.read_csv(full_path)
        print(f"[DataLoader] Successfully loaded data. Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"[DataLoader] Error loading data: {e}")
        return None
