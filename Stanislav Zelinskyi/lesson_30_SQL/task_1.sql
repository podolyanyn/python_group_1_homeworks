-- Create a new table
CREATE TABLE sample_table (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

-- Rename the table
ALTER TABLE sample_table RENAME TO renamed_table;

-- Add a new column
ALTER TABLE renamed_table ADD COLUMN email TEXT;

-- Insert rows into the table
INSERT INTO renamed_table (name, age, email) VALUES ('John', 25, 'john@example.com');
INSERT INTO renamed_table (name, age, email) VALUES ('Sarah', 30, 'sarah@example.com');

-- Update a row
UPDATE renamed_table SET age = 26 WHERE id = 1;

-- Delete a row
DELETE FROM renamed_table WHERE id = 2;
