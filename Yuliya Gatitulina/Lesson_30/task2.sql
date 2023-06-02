select first_name as 'First Name', last_name as "Last Name" from employees;
select distinct department_id from employees;
select * from employees order by first_name desc;
select first_name, last_name, salary, salary*0.12 as PF from employees;
select min(salary) as min_salary, max(salary)  as max_salary from employees;
select first_name, last_name, round(salary / 12.0, 2) as monthly_salary from employees;
