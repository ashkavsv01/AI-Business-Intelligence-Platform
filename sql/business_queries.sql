-- AI-Powered Retail Business Intelligence Platform

SELECT * FROM sales LIMIT 10;
SELECT SUM(Sales) AS Total_Sales FROM sales;
SELECT SUM(Profit) AS Total_Profit FROM sales;

SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

SELECT Category, SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;

SELECT Segment, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Segment
ORDER BY Total_Sales DESC;

SELECT "Customer Name", SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Customer Name"
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT "Product Name", SUM(Sales) AS Total_Sales
FROM sales
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT State, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY State
ORDER BY Total_Sales DESC;

SELECT AVG(Sales) AS Average_Sales,
AVG(Profit) AS Average_Profit
FROM sales;

SELECT "Ship Mode", COUNT("Order ID") AS Total_Orders
FROM sales
GROUP BY "Ship Mode"
ORDER BY Total_Orders DESC;
