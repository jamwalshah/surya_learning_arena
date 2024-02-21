SHOW DATABASES;

-- create a database called mydb
CREATE DATABASE mydb;
USE mydb;
SHOW TABLES;

-- create the table
CREATE TABLE emp(id int, name varchar(30), sal int);
SELECT * FROM emp; -- it should have no data initially

  -- Insert data into table emp before reading
INSERT INTO emp VALUES (1, 'John', 10000);
INSERT INTO emp VALUES (2, 'Bob', 20000);
-- INSERT INTO emp VALUES (3, 'Abhy', 30000) ;

-- DELETE FROM emp WHERE id='%d' ;

-- UPDATE emp SET sal='%d' WHERE id='%d' ;

drop database mydb;