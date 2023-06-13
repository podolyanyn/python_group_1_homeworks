CREATE TABLE My_Table(
    Column_ID int,
    Column_1 varchar,
    Column_2 varchar,
    Column_3 varchar
); -- create a table named "My_Table" with columns "Column_ID" of type int, "Column_1" of type varchar, "Column_2" of
-- type varchar, "Column_3" of type varchar

SELECT * FROM My_Table;  -- select all columns and all rows from table "My_Table"

ALTER TABLE My_Table
ADD Column_4 varchar;  -- add a new column "Column_4" of type varchar to the table "My_Table"

INSERT INTO My_Table (Column_1, Column_2, Column_3, Column_4)
VALUES ('Frostwolf clan','Warsong clan','Blackrock clan','Bleeding Hollow clan'); -- insert the corresponding words in
-- the corresponding columns

INSERT INTO My_Table (Column_1, Column_2, Column_3, Column_4) -- insert the corresponding words in the corresponding
-- columns
VALUES ('Bloodhoof tribe','Ragetotem tribe','Dawnstrider tribe','Runetotem tribe');

UPDATE My_Table
SET Column_ID='Orkish clans'
WHERE Column_1='Frostwolf clan';  -- update the table and set the value in the Column_id column for rows where the value
-- is Frostwolf clan

UPDATE My_Table
SET Column_ID='Tauren tribes'
WHERE Column_1='Bloodhoof tribe';

DELETE FROM My_Table WHERE Column_2='Ragetotem tribe' -- deletes the row in which there is a column with the value
-- "Ragetotem tribe"