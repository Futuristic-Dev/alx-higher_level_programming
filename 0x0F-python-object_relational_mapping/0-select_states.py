#!/usr/bin/python3


"""
A script that lists all the states from the database, hbtn_0e_0_usa.\n

Parameters for the script: username, passwword and database.
"""



import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Establish a secure a connection to the server."""
    db = MySQL.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    """Create a cursor object to execute SQL queries."""
    cursor = db.cursor()

    """Execute the cursor tpo retrieve."""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

        cursor.close()
        db.close()
