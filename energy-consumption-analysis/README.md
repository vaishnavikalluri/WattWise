# WattWise Energy Consumption Analysis

A production-style data analytics project that analyzes state-wise electricity consumption data, detects anomalies, and presents insights through a Flask dashboard.

## Table of Contents
1. Project Overview
2. Key Features
3. Tech Stack
4. Repository Structure
5. Getting Started After Cloning
6. Usage
7. Data Dictionary and Transformation Logic
8. Outputs You Will See
9. Module-by-Module Breakdown
10. Limitations and Improvement Ideas
11. Contributing

## Project Overview
WattWise is an end-to-end analytics workflow for electricity usage data.

The project:
1. Loads raw consumption records from CSV.
2. Cleans and prepares the data for analysis.
3. Computes trend and peak-load insights.
4. Uses machine learning to identify abnormal consumption spikes.
5. Generates visual plots and serves them through a web interface.

This repository is suitable for portfolio demonstration, academic submission, and beginner-to-intermediate learning of data + web integration.


## Key Features
1. State-wise and time-wise consumption analysis.
2. Peak load identification (global and state-level context).
3. Monthly and daily trend support.
4. IsolationForest-based anomaly detection.
5. Auto-generated plot images in static folder.
6. Flask dashboard with KPI cards and dataset preview.
7. Scripted dataset setup from Kaggle source.

## Tech Stack

### Language
- Python

### Data and Analysis
- pandas: CSV loading, cleaning, grouping, aggregations.
- numpy: scientific stack dependency support.
- scikit-learn: IsolationForest model for anomaly detection.

### Visualization
- matplotlib: plot rendering and PNG export.
- seaborn: improved statistical visual styles.

### Web
- Flask: routes, template rendering, and dashboard serving.

### Data Acquisition
- kagglehub: download and copy source dataset into local data folder.

## Repository Structure
```text
energy-consumption-analysis/
├── app.py
├── main.py
├── setup_data.py
├── copy_image.py
├── requirements.txt
├── README.md
├── data/
│   └── dataset.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── analysis.py
│   ├── anomaly_detection.py
│   └── visualization.py
├── static/
│   ├── images/
│   └── plots/
└── templates/
    ├── home.html
    └── dashboard.html
```

## Getting Started After Cloning

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd energy-consumption-analysis
```

### 2. Create and Activate Virtual Environment (Recommended)

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Prepare Dataset
If data/dataset.csv already exists, you can skip this step.

To download from Kaggle source and place it automatically:
```bash
python setup_data.py
```

### 5. (Optional) Copy Hero Image Asset
If your homepage image is missing:
```bash
python copy_image.py
```

### 6. Run the Project
Command line analytics mode:
```bash
python main.py
```

Web dashboard mode:
```bash
python app.py
```

Then open:
```text
http://127.0.0.1:5000/
```

## Usage

### CLI Mode
Use CLI mode when you want analysis logs in terminal and generated plot files.

Expected behavior:
1. Data is loaded and preprocessed.
2. Peak and average values are printed.
3. Anomalies are detected.
4. Charts are regenerated in static/plots.

### Dashboard Mode
Use dashboard mode for presentation and visual interpretation.

Routes:
1. / : Landing dashboard with KPI cards and collapsible analytics blocks.
2. /dashboard : Alternate detailed dashboard layout with sectioned narrative.

## Data Dictionary and Transformation Logic

### Raw Dataset Columns
1. date: observation date.
2. state: region/state name.
3. consumption_mwh: power consumption in megawatt-hours.

### Preprocessing Rules
1. Convert date from string to datetime.
2. Fill missing values using forward fill.
3. Drop residual null rows.

### Analysis Rules
1. Peak load: maximum consumption row globally and per state.
2. Average consumption: mean consumption grouped by state.
3. Monthly trend: total consumption grouped by month period.
4. Daily trend: total consumption grouped by day.

### Anomaly Detection Rules
1. Train IsolationForest on consumption_mwh.
2. contamination=0.05 defines expected anomaly fraction.
3. Model output -1 mapped to boolean anomaly flag.

## Outputs You Will See

### Terminal Output
1. Data load success/failure and shape.
2. Preprocess completion message.
3. Peak record summary.
4. State-wise averages.
5. Anomaly count.
6. Plot generation confirmation.

### Generated Files
The following chart images are generated in static/plots:
1. electricity_over_time.png
2. state_consumption.png
3. monthly_trend.png
4. peak_load.png
5. anomalies.png

### Web Output
Dashboard shows:
1. Total consumption.
2. Average daily consumption.
3. Maximum peak load.
4. Number of detected anomalies.
5. Plot sections with interpretation text.
6. Preview table of processed rows.

## Module-by-Module Breakdown

### Root Scripts
1. app.py: Flask app entry, routes, runtime analytics, template rendering.
2. main.py: command-line pipeline runner.
3. setup_data.py: Kaggle download and CSV placement utility.
4. copy_image.py: helper script to place hero image in static/images.

### src Package
1. data_loader.py: resilient CSV loading from project-relative path.
2. preprocess.py: cleaning, datetime conversion, null handling.
3. analysis.py: peak, average, monthly and daily analytics helpers.
4. anomaly_detection.py: IsolationForest training and anomaly labeling.
5. visualization.py: all chart functions and save-to-static pipeline.

### Templates and Static
1. templates/home.html: primary landing dashboard.
2. templates/dashboard.html: detailed alternate dashboard.
3. static/plots: generated analytics images.
4. static/images: UI assets.

## Limitations and Improvement Ideas

Current limitations:
1. Anomaly model uses only one feature.
2. Plots regenerate on every dashboard request.
3. Data source is local CSV only.
4. Dashboard narrative text is mostly static.

Suggested improvements:
1. Add multi-feature anomaly model (state, lag features, rolling stats).
2. Add caching layer for plot generation.
3. Add API endpoints and a proper data service layer.
4. Add unit tests and CI workflow.
5. Add environment configuration via .env.

## Contributing
1. Fork and clone the project.
2. Create a feature branch.
3. Commit changes with clear messages.
4. Open a pull request with test notes and screenshots.

For major changes, open an issue first describing the scope and expected behavior.
