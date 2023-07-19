-- creates the MySQL server user user_0d_1
-- 	user_0d_1: have all privileges on the MySQL server
-- 	the script does not fail if the user user_0d_1 already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
