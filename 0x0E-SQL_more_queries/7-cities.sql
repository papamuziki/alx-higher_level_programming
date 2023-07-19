-- creates the database hbtn_0d_usa and the table cities(in database hbtn_0d_usa) on MySQL server
-- 	cities description:
-- 		id INT unique, auto generated, can’t be null and is a primary key
-- 		state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
-- 		name VARCHAR(256) can’t be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities`
(
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL UNIQUE,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY(state_id) REFERENCES state(id)
);
