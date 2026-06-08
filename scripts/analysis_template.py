#!/usr/bin/env python3
"""
Template for data analysis projects.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from data_utils import load_data, basic_stats, clean_missing_data, remove_duplicates

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)


def main():
    """
    Main analysis workflow.
    """
    
    # Step 1: Load data
    print("=" * 50)
    print("STEP 1: LOADING DATA")
    print("=" * 50)
    df = load_data('sample_data.csv')
    if df is None:
        return
    
    # Step 2: Explore data
    print("\n" + "=" * 50)
    print("STEP 2: EXPLORING DATA")
    print("=" * 50)
    basic_stats(df)
    
    # Step 3: Clean data
    print("\n" + "=" * 50)
    print("STEP 3: CLEANING DATA")
    print("=" * 50)
    df = clean_missing_data(df, method='fill')
    df = remove_duplicates(df)
    
    # Step 4: Analyze data
    print("\n" + "=" * 50)
    print("STEP 4: ANALYZING DATA")
    print("=" * 50)
    
    # Calculate statistics
    print(f"\nAverage Salary: ${df['Salary'].mean():.2f}")
    print(f"Median Salary: ${df['Salary'].median():.2f}")
    print(f"Salary Range: ${df['Salary'].min():.2f} - ${df['Salary'].max():.2f}")
    
    # Group analysis
    print("\nAverage Salary by Department:")
    print(df.groupby('Department')['Salary'].mean())
    
    # Step 5: Visualize data
    print("\n" + "=" * 50)
    print("STEP 5: VISUALIZING DATA")
    print("=" * 50)
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Salary distribution
    axes[0, 0].hist(df['Salary'], bins=10, color='#667eea', alpha=0.7)
    axes[0, 0].set_title('Salary Distribution')
    axes[0, 0].set_xlabel('Salary ($)')
    axes[0, 0].set_ylabel('Count')
    
    # Plot 2: Age vs Salary
    axes[0, 1].scatter(df['Age'], df['Salary'], color='#764ba2', s=100, alpha=0.6)
    axes[0, 1].set_title('Age vs Salary')
    axes[0, 1].set_xlabel('Age')
    axes[0, 1].set_ylabel('Salary ($)')
    
    # Plot 3: Salary by Department
    df.boxplot(column='Salary', by='Department', ax=axes[1, 0])
    axes[1, 0].set_title('Salary by Department')
    axes[1, 0].set_xlabel('Department')
    axes[1, 0].set_ylabel('Salary ($)')
    
    # Plot 4: Experience vs Salary
    axes[1, 1].scatter(df['Years_Experience'], df['Salary'], color='#f093fb', s=100, alpha=0.6)
    axes[1, 1].set_title('Experience vs Salary')
    axes[1, 1].set_xlabel('Years of Experience')
    axes[1, 1].set_ylabel('Salary ($)')
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "=" * 50)
    print("ANALYSIS COMPLETE")
    print("=" * 50)


if __name__ == "__main__":
    main()
