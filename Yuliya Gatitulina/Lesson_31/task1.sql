SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
LEFT JOIN departments ON employees.department_id=departments.department_id;

SELECT employees.first_name, employees.last_name, departments.depart_name, locations.city, locations.state_province
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
LEFT JOIN locations ON departments.location_id = locations.location_id;

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id
where employees.department_id in (80, 40);

SELECT departments.depart_name, employees.department_id, employees.first_name, employees.last_name
FROM departments
LEFT JOIN employees ON departments.department_id = employees.department_id;

SELECT A.first_name AS employee_name, B.first_name AS manager_name
FROM employees A
JOIN employees B
ON A.manager_id = B.employee_id;

SELECT jobs.job_title, employees.first_name || ' ' || employees.last_name AS 'full_name', jobs.max_salary - employees.salary AS gap_to_max_salary
FROM employees
LEFT JOIN jobs ON employees.job_id = jobs.job_id;

SELECT jobs.job_title, AVG(employees.salary)
FROM employees
NATURAL JOIN jobs
GROUP BY job_title;

SELECT employees.first_name || ' ' || employees.last_name AS 'full_name', employees.salary
FROM employees
JOIN departments ON employees.department_id = departments.department_id
JOIN locations ON departments.location_id = locations.location_id
where locations.city = 'London';

SELECT departments.depart_name, COUNT(employees.department_id) AS 'number_employees'
FROM departments
INNER JOIN employees ON employees.department_id = departments.department_id
GROUP BY departments.department_id, departments.depart_name
ORDER BY departments.depart_name;