import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('sql_hr.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define a SQL statement to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS offices (
    office_id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL
);
"""

# Execute the SQL statement to create the table
cursor.execute(create_table_query)

# Commit the transaction to save the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("SQLite database 'sql_hr.db' created successfully!")