-- Import database in table dump
SELECT city, temperature FROM temperatures WHERE month IN (7, 8) ORDER BY temperature DESC LIMIT 3;
