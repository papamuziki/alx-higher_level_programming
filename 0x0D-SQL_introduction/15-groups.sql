-- lists the number of records with the same score
CREATE DATABASE IF NOT EXISTS `hbtn_0c_0`;
use hbtn_0c_0;
SELECT score COUNT(score) AS 'number' FROM `second_table` GROUP BY score DESC;
