-- This script creates a table second_table in the database hbtn_0c_0
-- in your MySQL server and add multiples rows
--	second_table description:
--		id INT
--		name VARCHAR(256)
--		score INT
-- This script should not fail if second_table already exists
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
