-- Query 1: Display names with aliases
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

-- Query 2: Get unique department IDs
SELECT DISTINCT department_id
FROM employees;

-- Query 3: Get employee details ordered by first name, descending
SELECT *
FROM employees
ORDER BY first_name DESC;

-- Query 4: Get names, salary, and PF (12% of salary)
SELECT first_name, last_name, salary, salary * 0.12 AS PF
FROM employees;

-- Query 5: Get maximum and minimum salary
SELECT MAX(salary) AS max_salary, MIN(salary) AS min_salary
FROM employees;

-- Query 6: Get monthly salary (rounded to 2 decimal places)
SELECT first_name, last_name, ROUND(salary / 12, 2) AS monthly_salary
FROM employees;
