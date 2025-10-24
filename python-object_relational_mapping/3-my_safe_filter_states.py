#!/usr/bin/python3
""" List all states from the database safe from MySQL injection """
if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        exit

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                   WHERE BINARY name = '{}'
                   ORDER BY id ASC""".format(sys.argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
