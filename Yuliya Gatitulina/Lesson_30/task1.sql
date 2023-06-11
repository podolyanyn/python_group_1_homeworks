create table Population (country char(2), city varchar primary key, people_in_billions real);
alter table Population rename to Update_Population;
alter table Update_Population add average_age real;
insert into Update_Population (country, city, people_in_billions, average_age) values ('uk', 'London', 8.17, 33);
insert into Update_Population (country, city, people_in_billions, average_age) values ('it', 'Milan', 1.35, 48);
update Update_Population set average_age = 38 where country = 'uk';
delete from Update_Population where country = 'it';



