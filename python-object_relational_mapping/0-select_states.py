#!/usr/bin/python3
"""
List all states from the database
"""
import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, database="hbtn_0e_0_usa")
cursor=db.cursor()
cursor.execute("""SELECT * FROM states""")
result = cursor.fetchall()
for row in result:
    print(row)
