import pandas as pd
import numpy as np

def clean_and_engineer_features(df):
    """
    Performs data cleaning and feature engineering on the raw DataFrame.
    
    Args:
        df (pd.DataFrame): The raw DataFrame.
        
    Returns:
        pd.DataFrame: The processed DataFrame.
    """
    print("\n--- Data Cleaning and Feature Engineering ---")
    
    # 1. Convert 'date' to datetime and set as index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date').sort_index()
    
    # 2. Calculate Revenue
    # Assuming revenue = price_unit * units_sold
    df['revenue'] = df['price_unit'] * df['units_sold']
    
    # 3. Create Time-based features
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek # Monday=0, Sunday=6
    df['week_of_year'] = df.index.isocalendar().week.astype(int)
    
    # 4. Check for stockout events (simplified: units_sold > delivered_qty)
    # The dataset has 'delivered_qty' and 'stock_available'. 
    # A stockout could be inferred if delivered_qty is low and units_sold is also low, 
    # or if delivered_qty is 0. Given the data structure, focus on 
    # a simple metric: stock_available == 0 and units_sold > 0 (a sale was made despite no stock)
    # or just stock_available == 0 (potential lost sales).
    df['stockout_flag'] = np.where(df['stock_available'] == 0, 1, 0)
    
    print(f"Processed DataFrame shape: {df.shape}")
    print(f"New columns added: {['revenue', 'year', 'month', 'day_of_week', 'week_of_year', 'stockout_flag']}")
    
    return df

def perform_analysis(df):
    """
    Performs key FMCG data analysis and returns aggregated results.
    
    Args:
        df (pd.DataFrame): The processed DataFrame.
        
    Returns:
        dict: A dictionary containing key analysis results (DataFrames).
    """
    analysis_results = {}
    
    # 1. Overall Sales Trend (Daily Total Revenue)
    daily_sales = df.groupby(df.index)['revenue'].sum().rename('daily_revenue')
    analysis_results['daily_sales_trend'] = daily_sales
    
    # 2. Promotion Effectiveness
    promo_analysis = df.groupby('promotion_flag')['revenue'].agg(['sum', 'mean', 'count']).reset_index()
    promo_analysis.columns = ['promotion_flag', 'total_revenue', 'avg_revenue_per_transaction', 'transaction_count']
    analysis_results['promotion_effectiveness'] = promo_analysis
    
    # 3. Regional and Channel Performance
    region_channel_performance = df.groupby(['region', 'channel'])['revenue'].sum().reset_index()
    region_channel_performance = region_channel_performance.pivot_table(index='region', columns='channel', values='revenue', fill_value=0)
    analysis_results['region_channel_performance'] = region_channel_performance
    
    # 4. Top 10 Products (SKU) by Revenue
    top_products = df.groupby('sku')['revenue'].sum().nlargest(10).reset_index()
    top_products.columns = ['sku', 'total_revenue']
    analysis_results['top_10_products'] = top_products
    
    # 5. Stockout Impact (Total revenue lost due to stockout - simplified)
    # This is a very simplified view. A more complex model would be needed for true lost sales.
    # Just count the number of days/SKUs that experienced a stockout.
    stockout_count = df[df['stockout_flag'] == 1].shape[0]
    total_transactions = df.shape[0]
    stockout_rate = stockout_count / total_transactions
    
    stockout_summary = pd.DataFrame({
        'Metric': ['Total Stockout Occurrences (SKU-Day)', 'Total Transactions', 'Stockout Rate'],
        'Value': [stockout_count, total_transactions, f"{stockout_rate:.2%}"]
    })
    analysis_results['stockout_summary'] = stockout_summary
    
    print("\nAnalysis complete. Results stored in dictionary.")
    return analysis_results

if __name__ == '__main__':
    # Define the path to the downloaded data file
    data_file_path = 'data/FMCG_2022_2024.csv'
    
    # Load the data (using a simplified version of the loader for self-contained script)
    try:
        df_raw = pd.read_csv(data_file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {data_file_path}. Please ensure it is downloaded.")
        exit()
    
    # Process and engineer features
    df_processed = clean_and_engineer_features(df_raw.copy())
    
    # Perform analysis
    if df_processed is not None:
        results = perform_analysis(df_processed)
        
        # Print a sample of the results
        print("\n--- Sample Analysis Results ---")
        print("\nPromotion Effectiveness:")
        print(results['promotion_effectiveness'])
        print("\nRegional and Channel Performance (Total Revenue):")
        print(results['region_channel_performance'])
        print("\nTop 10 Products (SKU) by Revenue:")
        print(results['top_10_products'])
        print("\nStockout Summary:")
        print(results['stockout_summary'])
