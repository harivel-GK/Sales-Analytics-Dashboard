-- Sales analytics business queries
SELECT SUM(Revenue) AS TotalRevenue FROM sales;
SELECT COUNT(OrderID) AS TotalOrders FROM sales;
SELECT Region, SUM(Revenue) AS RegionRevenue FROM sales GROUP BY Region ORDER BY RegionRevenue DESC;
SELECT Product, SUM(Revenue) AS ProductRevenue FROM sales GROUP BY Product ORDER BY ProductRevenue DESC LIMIT 5;
SELECT Product, SUM(Quantity) AS TotalQuantity FROM sales GROUP BY Product ORDER BY TotalQuantity DESC LIMIT 5;
SELECT Year, Month, SUM(Revenue) AS MonthlyRevenue FROM sales GROUP BY Year, Month ORDER BY Year, Month;
SELECT AVG(Revenue) AS AverageOrderValue FROM sales;
SELECT CustomerID, COUNT(OrderID) AS OrderCount FROM sales GROUP BY CustomerID ORDER BY OrderCount DESC LIMIT 10;
SELECT DayOfWeek, SUM(Revenue) AS DailyRevenue FROM sales GROUP BY DayOfWeek ORDER BY DayOfWeek;
SELECT IsWeekend, SUM(Revenue) AS Revenue FROM sales GROUP BY IsWeekend;
SELECT Discount, SUM(Revenue) AS TotalRevenue FROM sales GROUP BY Discount ORDER BY Discount;
SELECT CustomerID, SUM(Revenue) AS LifetimeValue FROM sales GROUP BY CustomerID ORDER BY LifetimeValue DESC LIMIT 10;
SELECT Region, AVG(Discount) AS AvgDiscount FROM sales GROUP BY Region;
SELECT Product, SUM(Revenue) AS Revenue FROM sales GROUP BY Product ORDER BY Revenue ASC LIMIT 1;
WITH MonthlySales AS (SELECT Year, Month, SUM(Revenue) AS Rev FROM sales GROUP BY Year, Month)
SELECT Year, Month, Rev, LAG(Rev) OVER(ORDER BY Year, Month) AS PrevMonthRev,
       ((Rev - LAG(Rev) OVER(ORDER BY Year, Month)) / NULLIF(LAG(Rev) OVER(ORDER BY Year, Month), 0)) * 100 AS GrowthPct
FROM MonthlySales;
SELECT OrderID, Product, Discount, Revenue FROM sales WHERE Discount >= 0.15;
SELECT Product, AVG(UnitPrice) AS AvgPrice FROM sales GROUP BY Product;
SELECT Region, COUNT(DISTINCT CustomerID) AS UniqueCustomers FROM sales GROUP BY Region;
SELECT Year, SUM(Revenue) AS AnnualRevenue FROM sales GROUP BY Year ORDER BY Year;
