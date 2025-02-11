#Write a Python program to connect to an SQLite3 database, create a table,
#  insert data, and fetch data. 

import sqlite3

dbcon = sqlite3.connect("newdb1.db")
print("Database is created successfully")

create_TB = "create table student2(id int primary key,fname text,lname text,course text)"
dbcon.execute(create_TB)
print("Table is created successfully")

data = "insert into student2 values(1,'dhruvit','savaliya','bca'),(2,'vivek','dalsaniya','bba'),(3,'smit','patel','bcom')"
dbcon.execute(data)
print("Data insert successfully")

fetch = dbcon.cursor()
fetch.execute("select * from student2")
rows=fetch.fetchall()
for row in rows:
    print(row)