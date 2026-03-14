import os
import kagglehub
import shutil

# Download latest version
path = kagglehub.dataset_download("twinkle0705/state-wise-power-consumption-in-india")

print("Path to dataset files:", path)

target_dir = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "dataset.csv")

for root, dirs, files in os.walk(path):
    for str_file in files:
        if str_file.endswith(".csv"):
            shutil.copy(os.path.join(root, str_file), target_file)
            print("Copied", str_file, "to data/dataset.csv")
            break
