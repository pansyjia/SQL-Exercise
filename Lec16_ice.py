import sqlite3

conn = sqlite3.connect('Northwind_small.sqlite')
cur = conn.cursor()


statement1 = '''
SELECT r.Id, r.ShippedDate, e.LastName, e.FirstName, e.HomePhone
FROM [Order] As r
  JOIN Employee As e
     ON r.EmployeeId = e.Id
'''
cur.execute(statement1)
print("--------------- Results of Q1 ---------------")
for row in cur:
    print(row)


statement2 = '''
SELECT r.Id, r.Freight
FROM [Order] As r
  JOIN Shipper As sh
     ON r.ShipVia = sh.Id
WHERE r.Freight > 100 AND sh.CompanyName = "United Package"
'''
cur.execute(statement2)
print("--------------- Results of Q2 ---------------")
for row in cur:
    print(row)


statement3 = '''
SELECT c.CompanyName, c.Country
FROM Customer As c
  JOIN [Order] As r
     ON c.Id = r.CustomerId
WHERE r.ShippedDate Like "2012-10-%"
'''

cur.execute(statement3)
print(" --------------- Results of Q3 ---------------")
for row in cur:
    print(row)


statement4 = '''
SELECT LastName, FirstName
FROM Employee
WHERE ID = 2
'''
cur.execute(statement4)

statement5 = '''
SELECT e.LastName, e.FirstName
FROM Employee AS e
  JOIN Employee AS boss
  On e.ReportsTo = boss.Id
WHERE boss.Title = "Vice President, Sales"
'''
cur.execute(statement5)
print(" --------------- Results of Q4 ---------------")
for row in cur:
    print(row[0] + " " + row[1] + ", Fuller Andrew")





conn.close()
