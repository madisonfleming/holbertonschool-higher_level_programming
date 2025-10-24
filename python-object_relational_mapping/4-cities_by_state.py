#!/usr/bin/python3
""" List cities from the database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    for a in sys.argv:
        if a.count(";"):
            exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   ORDER BY id ASC""")
    result = cursor.fetchall()
    for row in result:
        print(row)
