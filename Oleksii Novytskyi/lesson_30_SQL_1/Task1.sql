create table Dishes (id integer primary key, name text, quantity integer);
alter table Dishes RENAME to Food;
alter table Food
add status text;
insert into Food (id, name, quantity, status)
values (1, 'Banana', 10, 'ready');
insert into Food (id, name, quantity, status)
values (2, 'kakes', 15, 'ready');
insert into Food (id, name, quantity, status)
values (3, 'Burger', 15, 'ready');
update Food
set name = 'apple'
where id = 1;
delete from Food
where id = 3;
