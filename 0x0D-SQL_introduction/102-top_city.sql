-- Import database in table dump
SELECT city, AVG(value) AS avf_temperature
FROM temperatures 
WHERE month  BETWEEN ('7' AND '8')
GROUP BY city
ORDER BY avg_temperature DESC LIMIT 3;
