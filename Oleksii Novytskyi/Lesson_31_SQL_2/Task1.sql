SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
LEFT JOIN departments ON employees.department_id=departments.department_id;

SELECT employees.first_name, employees.last_name, departments.depart_name, locations.city, locations.state_province
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
LEFT JOIN locations on departments.location_id = locations.location_id;

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id
where employees.department_id in (80, 40)  ;

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
FULL JOIN departments ON employees.department_id = departments.department_id;

SELECT E.first_name AS "Employee Name",
M.first_name AS "Manager Name"
FROM employees E
JOIN employees M
ON E.manager_id = M.employee_id;

SELECT jobs.job_title, employees.first_name || ' ' || employees.last_name AS 'Full Name', jobs.max_salary - employees.salary AS 'Possible salary up'
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id;

SELECT jobs.job_title, AVG(employees.salary)
FROM employees
NATURAL JOIN jobs
GROUP BY job_title;

SELECT employees.first_name || ' ' || employees.last_name AS 'Full Name', employees.salary
FROM employees
JOIN departments ON employees.department_id = departments.department_id
JOIN locations on departments.location_id = locations.location_id
where locations.city = 'London';

SELECT departments.depart_name, COUNT(employees.department_id) AS 'Number of employees'
FROM departments
INNER JOIN employees ON employees.department_id = departments.department_id
GROUP BY departments.department_id, departments.depart_name
ORDER BY departments.depart_name;







