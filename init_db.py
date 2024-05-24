import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="falsk_db",
        user='shivesh',
        password='password')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this drops the table if it exists and then creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('''
    CREATE TABLE users (
        id serial PRIMARY KEY,
        first_name varchar(150) NOT NULL,
        last_name varchar(150) NOT NULL,
        company varchar(150) NOT NULL,
        age integer NOT NULL,
        city varchar(150) NOT NULL,
        state varchar(150),
        zip varchar(150) NOT NULL,
        email varchar(150),
        web varchar(150)
    );
''')

# Insert data into the table
cur.execute('''
    INSERT INTO users (first_name, last_name, company, age, city, state, zip, email, web)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
''', (
    'Aman',
    'Sharma',
    'Company 1',
    48,
    'Lko',
    'UP',
    '256489',
    'aman@gmail.com',
    'aman.dev.com'
))

conn.commit()

cur.close()
conn.close()
