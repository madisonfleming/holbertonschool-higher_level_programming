#!/usr/bin/python3
""" List cities from the database and take the state name as an argument"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    for a in sys.argv:
        if a.count(";"):
            exit()

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    state_name = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
                   FROM cities
                   INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = '{}'
                   ORDER BY cities.id ASC""".format(state_name))
    result = cursor.fetchall()
    # result = str(result).replace("()", "")
    for city in result:
        print("{}, ".format(city[0]), end="")
