import sqlite3
import csv
import sys

def init_db():
    conn = sqlite3.connect('airports.sqlite')
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'Airports';
    '''
    cur.execute(statement)

    conn.commit()

    statement = '''
    CREATE TABLE 'Airports' (
        'Iata' TEXT PRIMARY KEY,
        'Airport' TEXT NOT NULL,
        'City' TEXT NOT NULL,
        'State' TEXT NOT NULL,
        'Country' TEXT NOT NULL,
        'Lat' INTEGER NOT NULL,
        'Long'INTEGER NOT NULL,
        'Cnt'INTEGER NOT NULL
        );
    '''

    cur.execute(statement)

    conn.commit()
    conn.close()



def insert_stuff():
    conn = sqlite3.connect('airports.sqlite')
    cur = conn.cursor()

    f = open('2011_february_us_airport_traffic.csv')
    csv_data = csv.reader(f)

    for row in csv_data:
        if row[0]!="iata":
            insertion = (None, row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[7])
            statement = 'INSERT INTO "Airports" '
            statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'

        cur.execute(statement, insertion)


    conn.commit()
    conn.close()


if len(sys.argv) > 1 and sys.argv[1] == '--init':
    print('Deleting db and starting over from scratch.')
    init_db()
else:
    print('Leaving the DB alone.')
    insert_stuff()
