#Write a Python program to insert data into an SQLite3 database and fetch it. 

import sqlite3

dbcon = sqlite3.connect("stud_db.db")

data = "insert into student values(1,'dhruvit','savaliya','bca'),(2,'vivek','dalsaniya','bba'),(3,'smit','patel','bcom')"
dbcon.execute(data)
print("Data insert successfully")

fetch = dbcon.cursor()
fetch.execute("select * from student")
rows=fetch.fetchall()
for row in rows:
    print(row)