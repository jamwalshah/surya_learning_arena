-- creates database
CREATE DATABASE employeedb;
-- uses database employeedb
\c employeedb;
-- creates table
-- id column will be auto-incremented as it is a sequence
CREATE TABLE employee (id SERIAL PRIMARY KEY, name VARCHAR(30), sal REAL); 
-- creates user(role)
CREATE USER test WITH ENCRYPTED PASSWORD 'password';
-- grant database level privileges to user 'test'
GRANT ALL PRIVILEGES ON DATABASE employeedb TO test;
-- grant table permission to user 'test'
GRANT ALL PRIVILEGES ON TABLE employee TO test;
-- grant permission of sequence created internally to user 'test'
-- postgres internally creates a sequnce named 'employee_id_seq' , to which user 'test' should have
-- otherwise it'll show error that 'test' user does not have access to the sequence rendering us 
-- unable to increment the value of 'id' column when you use the user 'test'
GRANT ALL PRIVILEGES ON SEQUENCE employee_id_seq TO test;


-- shows all records from employee table
SELECT * FROM employee;

INSERT INTO employee (name, sal) VALUES ('Surya', 20000);
SELECT * FROM employee;
UPDATE employee SET sal=30000 WHERE id='2';
DELETE FROM employee WHERE id = 2; 
DELETE FROM employee WHERE name='Surya';


-- DROP DATABASE employeedb
-- DROP USER test
-- Delete rows from table 'employee'
