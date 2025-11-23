import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from data_processor import clean_and_engineer_features, perform_analysis

# Define the output directory for figures
FIGURES_DIR = 'output/figures'
os.makedirs(FIGURES_DIR, exist_ok=True)
    
def plot_sales_trend(daily_sales_trend):
    """
    Plots the daily total revenue trend over time.
    """
    plt.figure(figsize=(14, 6))
    daily_sales_trend.plot(title='Daily Total Revenue Trend (2022-2024)', color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Total Revenue')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'daily_sales_trend.png'))
    plt.close()
    print(f"Saved: {os.path.join(FIGURES_DIR, 'daily_sales_trend.png')}")

def plot_promotion_effectiveness(promo_analysis):
    """
    Plots the promotion effectiveness based on total revenue.
    """
    plt.figure(figsize=(8, 6))
    sns.barplot(x='promotion_flag', y='total_revenue', data=promo_analysis)
    plt.title('Total Revenue: Promoted vs. Non-Promoted')
    plt.xlabel('Promotion Flag (0: No Promo, 1: Promo)')
    plt.ylabel('Total Revenue (in millions)')
    plt.xticks([0, 1], ['No Promotion', 'With Promotion'])
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'promotion_effectiveness.png'))
    plt.close()
    print(f"Saved: {os.path.join(FIGURES_DIR, 'promotion_effectiveness.png')}")

def plot_region_channel_performance(region_channel_performance):
    """
    Plots the regional and channel performance as a heatmap.
    """
    plt.figure(figsize=(10, 7))
    sns.heatmap(region_channel_performance, annot=True, fmt=".2f", cmap="YlGnBu", linewidths=.5, linecolor='black', cbar_kws={'label': 'Total Revenue'})
    plt.title('Regional and Channel Performance (Total Revenue)')
    plt.xlabel('Sales Channel')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'region_channel_performance.png'))
    plt.close()
    print(f"Saved: {os.path.join(FIGURES_DIR, 'region_channel_performance.png')}")

def plot_top_products(top_products):
    """
    Plots the top 10 products by total revenue.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='total_revenue', y='sku', data=top_products.sort_values(by='total_revenue', ascending=False), palette='viridis')
    plt.title('Top 10 Products (SKU) by Total Revenue')
    plt.xlabel('Total Revenue')
    plt.ylabel('SKU')
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, 'top_10_products.png'))
    plt.close()
    print(f"Saved: {os.path.join(FIGURES_DIR, 'top_10_products.png')}")

def main():
    # Define the path to the downloaded data file
    data_file_path = 'data/FMCG_2022_2024.csv'
    
    # Load the data (using a simplified version of the loader for self-contained script)
    try:
        df_raw = pd.read_csv(data_file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {data_file_path}. Please ensure it is downloaded.")
        return
    
    # Process and engineer features
    df_processed = clean_and_engineer_features(df_raw.copy())
    
    # Perform analysis
    if df_processed is not None:
        results = perform_analysis(df_processed)
        
        # Generate visualizations
        print("\n--- Generating Visualizations ---")
        plot_sales_trend(results['daily_sales_trend'])
        plot_promotion_effectiveness(results['promotion_effectiveness'])
        plot_region_channel_performance(results['region_channel_performance'])
        plot_top_products(results['top_10_products'])

if __name__ == '__main__':
    main()
