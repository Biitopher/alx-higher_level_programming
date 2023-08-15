-- Import database
SELECT city, AVG(temperature) AS avg_temperature_fahrenheit
FROM temperature_data
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
