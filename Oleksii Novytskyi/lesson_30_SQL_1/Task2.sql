-- create table Dishes (id integer primary key, name text, quantity integer);
-- alter table Dishes RENAME to Food;
-- alter table Food
-- add status text;
-- insert into Food (id, name, quantity, status)
-- values (1, 'Banana', 10, 'ready');
-- insert into Food (id, name, quantity, status)
-- values (2, 'kakes', 15, 'ready');
-- insert into Food (id, name, quantity, status)
-- values (3, 'Burger', 15, 'ready');
-- update Food
-- set name = 'apple'
-- where id = 1;
-- delete from Food
-- where id = 3;



SELECT first_name AS 'First Name', last_name AS "Last Name"
FROM employees;

SELECT DISTINCT department_id
FROM employees;

SELECT *
FROM employees
ORDER BY first_name DESC;

SELECT first_name, last_name, salary, salary*0.12 as PF
FROM employees;

SELECT MIN(salary) AS MINsalary, MAX(salary) AS MAXsalary
FROM employees;

SELECT first_name, last_name, round(salary/12.0, 2) as 'monthly salary'
FROM employees;


