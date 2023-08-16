-- Lists all cities in the database of california
SELECT id, 
name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California')
ORDER BY id;
