#Write a Python program to create a database and a table using SQLite3.

import sqlite3

dbcon = sqlite3.connect("stud_db.db")
print("Database is created successfully")

create_TB = "create table student(id int primary key,fname text,lname text,course text)"
dbcon.execute(create_TB)
print("Table is created successfully")