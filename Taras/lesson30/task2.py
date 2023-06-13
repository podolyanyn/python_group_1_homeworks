SELECT first_name AS "First Name", last_name AS "Last Name"  -- select columns "first_name" renamed to "First Name" and
-- "last_name" renamed to "Last Name"
FROM employees;  -- display the specified columns from the table employees

SELECT DISTINCT department_id  -- select unique values of field "department_id" from table "employees"
FROM employees;

SELECT *  -- select all fields from the "employees" table
FROM employees
ORDER BY first_name DESC;  -- sort the result by the field "first_name" in descending order (from Z to A)

SELECT first_name, last_name, salary, salary * 0.12 AS PF  -- select the fields "first_name", "last_name", "salary"
-- from the table "employees" and calculate the value of the "PF" field by multiplying "salary" by 0.12
FROM employees;

SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary  -- select highest salary (as "max_salary") and lowest
-- salary (as "min_salary") from the "employees" table
FROM employees;

SELECT first_name, last_name, ROUND(salary / 12, 2) AS monthly_salary  -- select fields "first_name", "last_name" from
-- table "employees" and calculate the value of the "monthly salary" field by dividing "salary" by 12 with rounding to 2
-- decimal places
FROM employees;