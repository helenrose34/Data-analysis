#!/usr/bin/env python3
"""
Utility functions for data analysis.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def load_data(filepath):
    """
    Load CSV data from file.
    
    Args:
        filepath (str): Path to CSV file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return None


def basic_stats(df):
    """
    Display basic statistics of a DataFrame.
    
    Args:
        df (pd.DataFrame): Input DataFrame
    """
    print("DataFrame Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)
    print("\nBasic Statistics:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())


def clean_missing_data(df, method='drop'):
    """
    Handle missing data.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        method (str): 'drop' or 'fill'
        
    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    if method == 'drop':
        return df.dropna()
    elif method == 'fill':
        return df.fillna(df.mean())
    else:
        raise ValueError("Method must be 'drop' or 'fill'")


def remove_duplicates(df):
    """
    Remove duplicate rows.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame without duplicates
    """
    duplicates_before = len(df)
    df_clean = df.drop_duplicates()
    duplicates_removed = duplicates_before - len(df_clean)
    print(f"Removed {duplicates_removed} duplicate rows")
    return df_clean


def detect_outliers(df, column, method='iqr'):
    """
    Detect outliers in a column.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        column (str): Column name
        method (str): 'iqr' or 'zscore'
        
    Returns:
        pd.DataFrame: Outliers
    """
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    elif method == 'zscore':
        z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
        return df[z_scores > 3]
    else:
        raise ValueError("Method must be 'iqr' or 'zscore'")


def scale_features(X, method='standard'):
    """
    Scale numerical features.
    
    Args:
        X (pd.DataFrame or np.ndarray): Features
        method (str): 'standard' or 'minmax'
        
    Returns:
        np.ndarray: Scaled features
    """
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    else:
        raise ValueError("Method must be 'standard' or 'minmax'")
    
    return scaler.fit_transform(X)


def correlation_matrix(df):
    """
    Calculate and display correlation matrix.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: Correlation matrix
    """
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.corr()


if __name__ == "__main__":
    # Example usage
    print("Data Analysis Utility Functions")
    print("Import this module to use the functions")
