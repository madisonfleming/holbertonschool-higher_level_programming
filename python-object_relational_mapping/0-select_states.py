#!/usr/bin/python3
""" List all states from the database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states""")
    result = cursor.fetchall()
    for row in result:
        print(row)
