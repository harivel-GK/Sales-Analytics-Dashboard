CREATE DATABASE IF NOT EXISTS sales_analytics;
USE sales_analytics;

CREATE TABLE IF NOT EXISTS sales (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    Product VARCHAR(100),
    Region VARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(12,2),
    Discount DECIMAL(5,2),
    CustomerID INT,
    Revenue DECIMAL(14,2),
    Year INT,
    Month INT,
    DayOfWeek INT,
    IsWeekend TINYINT
);
