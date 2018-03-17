import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()

statement = 'SELECT CompanyName '
statement += 'FROM Supplier '
statement += 'WHERE Region = \'Western Europe\''
cur.execute(statement)

print("--------Results of Q1--------")
for row in cur:
    print(row[0])

statement2 = 'SELECT ProductName '
statement2 += 'FROM Product '
statement2 += 'WHERE Discontinued = 0'
cur.execute(statement2)

print("--------Results of Q2--------")
for row in cur:
    print(row[0])


statement3 = 'SELECT FirstName, LastName '
statement3 += 'FROM Employee '
statement3 += 'WHERE ReportsTo = 2'
cur.execute(statement3)

print("--------Results of Q3--------")
for f,l in cur:
    print(f,l)

statement4 = 'SELECT OrderDate, ShippedDate '
statement4 += 'FROM [Order] '
statement4 += 'WHERE ShipCountry = \'USA\''
cur.execute(statement4)

print("--------Results of Q4--------")
for od,sd in cur:
    print(od,sd)

conn.close()
