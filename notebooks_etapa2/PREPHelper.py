import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def data_overview(df):
    print(f"Dataset shape: {df.shape}")
    
    print("\nData Types and Null Values:")
    print(df.info())
    
    print("\nData Summary (Descriptive Statistics):")
    print(df.describe())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nFirst 5 rows:")
    print(df.head())


def describe_variables(df):
    columns = ['PM10', 'NO2', 'CO', 'SO2', 'O3', 'PM2.5']
    print("\nDescription of variables:\n")
    
    for col in columns:
        print(f"Column: {col}")
        print(f"Description: Air quality pollutant concentration in µg/m³ (for PM10, PM2.5) or µg/m³ (for other gases).")
        print(f"Data Type: {df[col].dtype}")
        print(f"Possible values: Numeric, may include values of zero or negative numbers.")
        print(f"Missing values: {df[col].isnull().sum()} missing entries.")
        print('-' * 50)

def explore_quantitative_variables(df):
    columns = ['PM10', 'NO2', 'CO', 'SO2', 'O3', 'PM2.5']
    
    print("\nMeasures of Central Tendency:")
    for col in columns:
        print(f"{col} - Mean: {df[col].mean():.2f}, Median: {df[col].median():.2f}, Mode: {df[col].mode()[0]:.2f}")
    
    print("\nMeasures of Dispersion:")
    for col in columns:
        print(f"{col} - Range: {df[col].max() - df[col].min():.2f}, Variance: {df[col].var():.2f}, Std Dev: {df[col].std():.2f}")


sns.set_theme(style="whitegrid", palette="muted") 

sns.set_theme(style="whitegrid")

def visualize_outliers(df):
    columns = ['PM10', 'NO2', 'CO', 'SO2', 'O3', 'PM2.5']
    
    for col in columns:
        plt.figure(figsize=(8, 6))
        sns.boxplot(
            x=df[col],
            color="#FFB6C1",         # rosa suave
            fliersize=4,
            linewidth=1.5,
            boxprops=dict(alpha=0.7, edgecolor="black"),
            whiskerprops=dict(color="black"),
            capprops=dict(color="black"),
            medianprops=dict(color="darkred", linewidth=2)
        )
        plt.title(f"$Boxplot\ de\ {col}$", fontsize=14, fontweight="bold", color="black")
        plt.xlabel(f"{col} (µg/m³)", fontsize=12, color="black")
        sns.despine()
        plt.show()
        
        # Cálculo de outliers
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
        print(f"{col} - Outliers: {outliers.shape[0]} outliers")


def plot_histograms(df):
    columns = ['PM10', 'NO2', 'CO', 'SO2', 'O3', 'PM2.5']
    
    for col in columns:
        plt.figure(figsize=(8, 6))
        sns.histplot(
            df[col],
            kde=True,
            color="#FF69B4",   # rosa fuerte
            alpha=0.6,
            edgecolor="white"
        )
        plt.title(f"Histograma de {col}", fontsize=14, fontweight="bold", color="black")
        plt.xlabel(f"{col} (µg/m³)", fontsize=12, color="black")
        plt.ylabel("Frecuencia", fontsize=12, color="black")
        sns.despine()
        plt.show()

def plot_correlation_heatmap(df):
    corr_matrix = df[['PM10', 'NO2', 'CO', 'SO2', 'O3', 'PM2.5']].corr()
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap of Air Quality Variables")
    plt.show()

