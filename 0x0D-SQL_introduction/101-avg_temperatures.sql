-- Import database
SELECT city, ROUND(AVG((temperature * 9/5) + 32), 2) AS avg_temp_fahrenheit FROM weather GROUP BY city ORDER BY avg_temp_fahrenheit DESC;
