-- List all the cities in the database
SELECT cities.id, cities.name, states.name 
FROM cities, states
WHERE (cities.id = states.id)
ORDER BY cities.id ASC 
