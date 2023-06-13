SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees -- select the fields "first_name", "last_name", "department_id" from the table "employees" and the field
-- "depart_name" from the table "departments"
LEFT JOIN departments ON employees.department_id=departments.department_id;  -- сonnect data from the "employees" table
-- with data from the "departments" table (provided that the value of the "department_id" column in the "employees"
-- table matches the value of the "department_id" column in the "departments" table)

SELECT employees.first_name, employees.last_name, departments.depart_name, locations.city, locations.state_province
FROM employees -- Select fields "first_name", "last_name" from table "employees", field "depart_name" from table
-- "departments", fields "city" and "state_province" from table "locations"
LEFT JOIN departments ON employees.department_id = departments.department_id  -- connect data from the "employees"
-- table with data from the "departments" table (provided that the value of the "department_id" column in the
-- "employees" table matches the value of the "department_id" column in the "departments" table)
LEFT JOIN locations on departments.location_id = locations.location_id; -- connect data from the "departments" table
-- with data from the "locations" table (provided that the value of the "location_id" column in the "departments" table
-- matches the value of the "location_id" column in the "locations" table)

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees -- select the fields "first_name", "last_name", "department_id" from the table "employees" and the field
-- "depart_name" from the table "departments"
JOIN departments ON employees.department_id = departments.department_id -- сonnect data from the "employees" table with
-- data from the "departments" table ( provided that the value of the "department_id" column in the "employees" table
-- matches the value of the "department_id" column in the "departments" table)
where employees.department_id in (80, 40); -- select only those rows where the value of the "department_id" column in
-- the "employees" table is between 80 and 40

SELECT employees.first_name, employees.last_name, employees.department_id, departments.depart_name
FROM employees -- select the fields "first_name", "last_name", "department_id" from the table "employees" and the field
-- "depart_name" from the table "departments"
FULL JOIN departments ON employees.department_id = departments.department_id; -- connect data from the "employees" table
-- with data from the "departments" table(provided that the value of the "department_id" column in the "employees" table
-- matches the value of the "department_id" column in the "departments" table). Return all rows from both tables, even
-- if the "department_id" column values do not match

SELECT E.first_name AS "Employee Name", -- select the field "first_name" from the table "employees E" and give it the
-- alias "Employee Name"
M.first_name AS "Manager Name" -- select the field "first_name" from the table "employees Е" and give it the alias
-- "Manager Name"
FROM employees E
JOIN employees M
ON E.manager_id = M.employee_id;

SELECT jobs.job_title, employees.first_name || ' ' || employees.last_name AS 'Full Name',
       jobs.max_salary - employees.salary AS 'Possible salary up'
FROM employees -- select the "job_title" field from the "jobs" table and merge the "first_name" and "last_name" fields
-- from the "employees" table. Give the result an alias "Full Name". calculate the difference between "max_salary" from
-- the "jobs" table and "salary" from the "employees" table and give the result the alias "Possible salary up"
JOIN jobs ON employees.job_id = jobs.job_id; -- connect data from the "employees" table with data from the "jobs" table(
-- provided that the value of the "job_id" column in the "employees" table matches the value of the "job_id" column in
-- the "jobs" table)

SELECT jobs.job_title, AVG(employees.salary)
FROM employees -- select the field "job_title" from the table "jobs" and calculate the average value ("AVG") from the
-- field "salary" from the table "employees"
NATURAL JOIN jobs -- connect data from the "employees" table with data from the "jobs" table
GROUP BY job_title; -- perform data grouping by the "job_title" field

SELECT employees.first_name || ' ' || employees.last_name AS 'Full Name', employees.salary -- merge the "first_name" and
-- "last_name" fields from the "employees" table, give the result an alias "Full Name", select the "salary" field from
-- the "employees" table
FROM employees
JOIN departments ON employees.department_id = departments.department_id -- connect data from the "employees" table with
-- data from the "departments" table(provided that the value of the "department_id" column in the "employees" table
-- matches the value of the "department_id" column in the "departments" table)
JOIN locations on departments.location_id = locations.location_id -- connect data from the "departments" table with data
-- from the "locations" table(provided that the value of the "location_id" column in the "departments" table matches the
-- value of the "location_id" column in the "locations" table)
where locations.city = 'London'; -- select only those rows where the value of the "city" column in the "locations" table
-- is equal to 'London'

SELECT departments.depart_name, COUNT(employees.department_id) AS 'Number of employees'
FROM departments -- select the field "depart_name" from the table "departments" and calculate the number of rows
-- ("COUNT") from the field "department_id" in the table "employees"
INNER JOIN employees ON employees.department_id = departments.department_id -- connect data from the "departments" table
-- with data from the "employees" table(provided that the value of the "department_id" column in the "employees" table
-- matches the value of the "department_id" column in the "departments" table)
GROUP BY departments.department_id, departments.depart_name -- group data by "department_id" and "depart_name" columns
-- in the "departments" table
ORDER BY departments.depart_name; -- sort results by "depart_name" field