-- Selecting relevant columns and filtering data
SELECT Year, Year_Close, Annual_Percentage_Change
FROM gold_price_yearly_CLEANED
WHERE Year BETWEEN 2010 AND 2020; -- Filter data for a specific range of years

-- Joining tables
SELECT g.Year, g.Average_Closing_Price, e.Economic_Event
FROM gold_price_yearly_CLEANED g
JOIN economic_events e ON g.Year = e.Year; -- Assuming there's a table called 'economic_events' with columns 'Year' and 'Economic_Event'

-- Grouping data and calculating aggregates
SELECT Year, AVG(Average_Closing_Price) AS Avg_Price, MAX(Year_High) AS Max_High
FROM gold_price_yearly_CLEANED
GROUP BY Year
ORDER BY Year DESC; -- Calculate average closing price and maximum high price for each year, ordered by year in descending order

-- Filtering aggregated data
SELECT Year, AVG(Average_Closing_Price) AS Avg_Price
FROM gold_price_yearly_CLEANED
GROUP BY Year
HAVING AVG(Average_Closing_Price) > 1500; -- Filter years where average closing price is greater than 1500

-- Sorting results
SELECT *
FROM gold_price_yearly_CLEANED
ORDER BY Year ASC, Average_Closing_Price DESC; -- Order data by year in ascending order and average closing price in descending order
