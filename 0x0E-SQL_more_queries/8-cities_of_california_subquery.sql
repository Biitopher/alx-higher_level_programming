-- Lists all cities in the database of california
SELECT cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
