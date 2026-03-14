# Energy Consumption Analysis

An industry-style data science project built in Python that analyzes state-wise power consumption data. The project loads data, performs time-series analysis, detects anomalies, and visualizes the results on a Flask HTML dashboard.

## Project Structure
```text
energy-consumption-analysis
│
├── data
│   └── dataset.csv
│
├── src
│   ├── data_loader.py
│   ├── preprocess.py
│   ├── analysis.py
│   ├── anomaly_detection.py
│   └── visualization.py
│
├── templates
│   └── dashboard.html
│
├── static
│   └── plots
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## Dataset
The dataset tracks state-wise power consumption in India. It includes:
- `date`: The date of the recorded power consumption.
- `state`: The name of the Indian state.
- `consumption_mwh`: The power consumption measured in Megawatt-hours (MWh).

## Installation

1. Navigate to the project directory:
   ```bash
   cd energy-consumption-analysis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Project

### Command-Line Analysis
To run the analysis strictly in the terminal and generate statistical insights and plots:
```bash
python main.py
```
This script loads and preprocesses the data, runs analysis and anomaly detection, and saves the visualization graphs locally in `static/plots`.

### Web Dashboard
To load the visualizations interactively through a Flask web application dashboard:
```bash
python app.py
```
Then open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/). The dashboard properly sections the analysis into:
1. Consumption Over Time
2. State-wise Consumption Comparison
3. Monthly Trend
4. Peak Load Periods
5. Abnormal Consumption Spikes

## Methodology & Tools Used
* **Python**: Base language used.
* **Pandas**: Data manipulation, aggregation, indexing, and time-series extraction.
* **Scikit-Learn**: Implemented `IsolationForest` for unsupervised anomaly detection in electricity usage vectors.
* **Matplotlib & Seaborn**: Formatted graphs visually defining trends.
* **Flask**: Microframework rendering an interactive UI dashboard routing the resulting visualization graphics.
