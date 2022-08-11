-- lists all the cities of Cali
-- that are found on the database
USE hbtn_0d_usa;
SELECT id, name
	FROM states
	WHERE name = California
	ORDER BY cities.id;
