# Power BI Dashboard Specification

## Overview
Design requirements for an executive sales dashboard.

## Layout
- Header with title and last refreshed date
- KPI cards for revenue, orders, average order value, and average discount
- Monthly trend line chart and regional revenue donut chart
- Top products bar chart and product performance matrix
- Sidebar slicers for date, region, and product category

## KPI Measures
- Total Revenue: `SUM(Sales[Revenue])`
- Total Orders: `DISTINCTCOUNT(Sales[OrderID])`
- Average Order Value: `AVERAGE(Sales[Revenue])`
- Average Discount: `AVERAGE(Sales[Discount])`

## DAX Examples
```dax
Total Revenue = SUM(Sales[Revenue])
Previous Month Revenue = CALCULATE([Total Revenue], PREVIOUSMONTH(Calendar[Date]))
MoM Growth % = DIVIDE([Total Revenue] - [Previous Month Revenue], [Previous Month Revenue], 0)
YTD Revenue = TOTALYTD([Total Revenue], Calendar[Date])
```

## Visuals
- Monthly revenue trend
- Revenue by region
- Top five products by revenue
- Revenue decomposition by region and product
- Product matrix with quantity, revenue, and year-over-year growth
