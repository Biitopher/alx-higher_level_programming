-- Database import table dump
SELECT state, MAX(value) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state ASC;
