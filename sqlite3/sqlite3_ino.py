aaaaa


import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Step 1: Create table
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT
);
'''
cursor.execute(create_table_query)
print("Table 'users' created successfully.")

# Step 2: Drop table
drop_table_query = '''
DROP TABLE IF EXISTS users;
'''
cursor.execute(drop_table_query)
print("Table 'users' dropped successfully.")

# Step 3: Create table again for further operations
cursor.execute(create_table_query)
print("Table 'users' created again successfully.")

# Step 4: Alter table (adding a new column 'email')
# (Note: The column 'email' is already included in the create table step now)

# Step 5: Create a row (insert data)
create_row_query = '''
INSERT INTO users (name, age, email) VALUES (?, ?, ?);
'''
cursor.execute(create_row_query, ('John Doe', 30, 'john.doe@example.com'))
print("Row created successfully.")

# Step 6: Update a row
update_row_query = '''
UPDATE users SET age = ? WHERE name = ?;
'''
cursor.execute(update_row_query, (31, 'John Doe'))
print("Row updated successfully.")

# Step 7: Insert additional rows
additional_rows = [
    ('Jane Smith', 25, 'jane.smith@example.com'),
    ('Emily Johnson', 22, 'emily.johnson@example.com')
]
cursor.executemany(create_row_query, additional_rows)
print("Additional rows inserted successfully.")

# Step 8: Delete a row
delete_row_query = '''
DELETE FROM users WHERE name = ?;
'''
cursor.execute(delete_row_query, ('Jane Smith',))
print("Row deleted successfully.")

# Step 9: Select all records and print them
select_all_query = '''
SELECT * FROM users;
'''
cursor.execute(select_all_query)
rows = cursor.fetchall()

print("All records in the 'users' table:")
for row in rows:
    print(row)

# Commit changes and close the connection
conn.commit()
conn.close()
