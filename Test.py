import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# File path to the dataset
file_path = r'W:\Projects\CommTech\voip_data.csv'

# Load the dataset
df = pd.read_csv(file_path, parse_dates=['Timestamp'])

# Perform the analysis
def analyze_metrics(df):
    # Descriptive statistics
    stats_summary = df.describe()

    # Correlation matrix
    correlation_matrix = df.corr()

    # Simple regression analysis (impact of jitter and latency on packet loss)
    # Check if required columns exist
    if 'Jitter (ms)' in df.columns and 'Packet Loss (%)' in df.columns:
        jitter_slope, jitter_intercept, jitter_r_value, jitter_p_value, jitter_std_err = stats.linregress(df['Jitter (ms)'], df['Packet Loss (%)'])
        jitter_regression = (jitter_slope, jitter_intercept)
    else:
        jitter_regression = (None, None)
    
    if 'Latency (ms)' in df.columns and 'Packet Loss (%)' in df.columns:
        latency_slope, latency_intercept, latency_r_value, latency_p_value, latency_std_err = stats.linregress(df['Latency (ms)'], df['Packet Loss (%)'])
        latency_regression = (latency_slope, latency_intercept)
    else:
        latency_regression = (None, None)

    return stats_summary, correlation_matrix, jitter_regression, latency_regression

# Perform the analysis
stats_summary, correlation_matrix, jitter_regression, latency_regression = analyze_metrics(df)

# Print the statistics and correlation matrix
def print_report(stats_summary, correlation_matrix, jitter_regression, latency_regression):
    print("VoIP Signal Quality Analysis Report\n")
    
    print("Descriptive Statistics:")
    print(stats_summary)
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    
    if jitter_regression[0] is not None and jitter_regression[1] is not None:
        print("\nImpact of Jitter on Packet Loss:")
        print(f"Slope: {jitter_regression[0]:.2f}, Intercept: {jitter_regression[1]:.2f}")
    
    if latency_regression[0] is not None and latency_regression[1] is not None:
        print("\nImpact of Latency on Packet Loss:")
        print(f"Slope: {latency_regression[0]:.2f}, Intercept: {latency_regression[1]:.2f}")

# Generate and print the report
print_report(stats_summary, correlation_matrix, jitter_regression, latency_regression)
