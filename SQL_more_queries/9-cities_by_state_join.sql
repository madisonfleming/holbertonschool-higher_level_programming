-- List all the cities in the database
SELECT cities.id, cities.name, states.name FROM cities, states ORDER BY cities.id ASC
