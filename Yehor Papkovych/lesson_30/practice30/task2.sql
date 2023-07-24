SELECT first_name AS [First Name], last_name AS [Last Name]
FROM employees

SELECT first_name, last_name, department_id
FROM employees
WHERE department_id = 0

SELECT *
FROM employees
ORDER BY first_name DESC

SELECT first_name, last_name, salary, (salary * 0.12) as PF
FROM employees

SELECT MIN(salary)
FROM employees

SELECT MAX(salary)
FROM employees

SELECT first_name, last_name, salary, (salary * 0.12) as PF
FROM employees

SELECT first_name, last_name, ROUND((salary * (1 - commission_pct)), 2) as Monthly_Salary
FROM employees