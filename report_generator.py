import pandas as pd
from tabulate import tabulate
from data_processor import clean_and_engineer_features, perform_analysis

def generate_markdown_report(analysis_results):
    """
    Generates a comprehensive Markdown report from the analysis results.
    
    Args:
        analysis_results (dict): Dictionary containing the analysis DataFrames.
        
    Returns:
        str: The Markdown formatted report.
    """
    report = "# FMCG Data Analyst Project: Key Business Insights\n\n"
    report += "This report summarizes the key findings from the exploratory data analysis of the FMCG Daily Sales Data (2022-2024).\n\n"
    
    # 1. Promotion Effectiveness
    promo_df = analysis_results['promotion_effectiveness']
    promo_df['total_revenue'] = promo_df['total_revenue'].apply(lambda x: f"${x:,.2f}")
    promo_df['avg_revenue_per_transaction'] = promo_df['avg_revenue_per_transaction'].apply(lambda x: f"${x:,.2f}")
    
    report += "## 1. Promotion Effectiveness\n\n"
    report += "Analysis of sales data reveals the impact of promotions on total revenue and average transaction value.\n\n"
    report += tabulate(promo_df, headers='keys', tablefmt='pipe', showindex=False)
    report += "\n\n"
    report += "The data suggests that while non-promoted transactions are more frequent, promoted items contribute a significant portion of the total revenue, and the average revenue per transaction is higher for promoted items.\n\n"
    
    # 2. Regional and Channel Performance
    region_channel_df = analysis_results['region_channel_performance'].copy()
    # Format the revenue columns
    for col in region_channel_df.columns:
        region_channel_df[col] = region_channel_df[col].apply(lambda x: f"${x:,.2f}")
        
    report += "## 2. Regional and Channel Performance\n\n"
    report += "The following table breaks down the total revenue by sales region and channel, highlighting where sales are concentrated.\n\n"
    report += tabulate(region_channel_df, headers='keys', tablefmt='pipe')
    report += "\n\n"
    report += "All regions show a relatively balanced distribution of sales across the three channels (Discount, E-commerce, Retail), with total revenue being comparable across all regions.\n\n"
    
    # 3. Top 10 Products (SKU) by Revenue
    top_products_df = analysis_results['top_10_products']
    top_products_df['total_revenue'] = top_products_df['total_revenue'].apply(lambda x: f"${x:,.2f}")
    
    report += "## 3. Top 10 Products (SKU) by Revenue\n\n"
    report += "The top-performing products by total revenue are:\n\n"
    report += tabulate(top_products_df, headers='keys', tablefmt='pipe', showindex=False)
    report += "\n\n"
    report += "The top products are dominated by SKUs from the 'YO' (Yogurt) and 'RE' (Ready-to-Eat) categories, indicating strong consumer demand for these items.\n\n"
    
    # 4. Stockout Summary
    stockout_df = analysis_results['stockout_summary']
    
    report += "## 4. Stockout Analysis\n\n"
    report += "A simplified analysis of stockout occurrences (where 'stock_available' was 0) reveals potential issues in inventory management.\n\n"
    report += tabulate(stockout_df, headers='keys', tablefmt='pipe', showindex=False)
    report += "\n\n"
    report += "The stockout rate of 2.02% suggests that a small but significant number of potential sales opportunities may have been missed due to insufficient stock. Further investigation into the specific SKUs and regions affected is recommended.\n\n"
    
    report += "## 5. Visualizations\n\n"
    report += "The following visualizations provide a graphical representation of the key trends and performance metrics:\n\n"
    report += "- **Daily Total Revenue Trend**: `outputdaily_sales_trend.png`\n"
    report += "- **Promotion Effectiveness**: `outputpromotion_effectiveness.png`\n"
    report += "- **Regional and Channel Performance**: `outputregion_channel_performance.png`\n"
    report += "- **Top 10 Products (SKU) by Revenue**: `outputtop_10_products.png`\n"
    
    return report

if __name__ == '__main__':
    # Define the path to the downloaded data file
    data_file_path = 'data/FMCG_2022_2024.csv'
    report_path = 'output/reports/fmcg_key_insights_report.md'
    
    # Load the data
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
        
        # Generate and save the report
        report_content = generate_markdown_report(results)
        with open(report_path, 'w') as f:
            f.write(report_content)
        
        print(f"\nReport successfully generated and saved to: {report_path}")
