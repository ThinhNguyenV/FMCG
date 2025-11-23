# FMCG Data Analyst Project: Key Business Insights

This report summarizes the key findings from the exploratory data analysis of the FMCG Daily Sales Data (2022-2024).

## 1. Promotion Effectiveness

Analysis of sales data reveals the impact of promotions on total revenue and average transaction value.

|   promotion_flag | total_revenue   | avg_revenue_per_transaction   |   transaction_count |
|-----------------:|:----------------|:------------------------------|--------------------:|
|                0 | $14,849,830.28  | $91.50                        |              162296 |
|                1 | $5,101,470.30   | $179.24                       |               28461 |

The data suggests that while non-promoted transactions are more frequent, promoted items contribute a significant portion of the total revenue, and the average revenue per transaction is higher for promoted items.

## 2. Regional and Channel Performance

The following table breaks down the total revenue by sales region and channel, highlighting where sales are concentrated.

| region     | Discount      | E-commerce    | Retail        |
|:-----------|:--------------|:--------------|:--------------|
| PL-Central | $2,194,005.17 | $2,209,737.74 | $2,217,107.34 |
| PL-North   | $2,224,943.26 | $2,212,349.04 | $2,226,928.22 |
| PL-South   | $2,223,324.68 | $2,231,348.63 | $2,211,556.50 |

All regions show a relatively balanced distribution of sales across the three channels (Discount, E-commerce, Retail), with total revenue being comparable across all regions.

## 3. Top 10 Products (SKU) by Revenue

The top-performing products by total revenue are:

| sku    | total_revenue   |
|:-------|:----------------|
| YO-029 | $931,878.44     |
| YO-005 | $913,420.95     |
| YO-012 | $899,410.48     |
| MI-026 | $796,853.75     |
| RE-004 | $792,286.33     |
| YO-014 | $786,740.68     |
| YO-001 | $777,399.30     |
| RE-007 | $771,396.59     |
| RE-015 | $759,512.43     |
| YO-009 | $755,334.62     |

The top products are dominated by SKUs from the 'YO' (Yogurt) and 'RE' (Ready-to-Eat) categories, indicating strong consumer demand for these items.

## 4. Stockout Analysis

A simplified analysis of stockout occurrences (where 'stock_available' was 0) reveals potential issues in inventory management.

| Metric                               | Value   |
|:-------------------------------------|:--------|
| Total Stockout Occurrences (SKU-Day) | 3860    |
| Total Transactions                   | 190757  |
| Stockout Rate                        | 2.02%   |

The stockout rate of 2.02% suggests that a small but significant number of potential sales opportunities may have been missed due to insufficient stock. Further investigation into the specific SKUs and regions affected is recommended.

## 5. Visualizations

The following visualizations provide a graphical representation of the key trends and performance metrics:

- **Daily Total Revenue Trend**: `output/daily_sales_trend.png`
- **Promotion Effectiveness**: `output/promotion_effectiveness.png`
- **Regional and Channel Performance**: `output/region_channel_performance.png`
- **Top 10 Products (SKU) by Revenue**: `output/top_10_products.png`
