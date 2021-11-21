-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California (but the id can be different)
-- Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE name='California') ORDER BY id;
