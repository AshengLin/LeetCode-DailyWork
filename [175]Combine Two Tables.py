# Table: Person 
# 
#  
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | PersonId    | int     |
# | FirstName   | varchar |
# | LastName    | varchar |
# +-------------+---------+
# PersonId is the primary key column for this table.
#  
# 
#  Table: Address 
# 
#  
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | AddressId   | int     |
# | PersonId    | int     |
# | City        | varchar |
# | State       | varchar |
# +-------------+---------+
# AddressId is the primary key column for this table.
#  
# 
#  
# 
#  Write a SQL query for a report that provides the following information for ea
# ch person in the Person table, regardless if there is an address for each of tho
# se people: 
# 
#  
# FirstName, LastName, City, State
#  
#  Related Topics Database 
#  👍 1419 👎 166


# There is no code of Python3 type for this problem
import sqlite3
import pandas as pd
conn = sqlite3.connect("data.db")
c = conn.cursor()


c.execute('''CREATE TABLE Person(PersonId INT PRIMARY KEY NOT NULL, FirstName varchar NOT NULL, LastName varchar NOT NULL);''')

c.execute('''CREATE TABLE Address(AddressId INT PRIMARY KEY NOT NULL,PersonId varchar NOT NULL, City varchar NOT NULL, State varchar NOT NULL); ''')

results = c.execute('''select FirstName, LastName, City, State from Person left join Address on Person.PersonId = Address.PersonId''')

rows = c.fetchall()
for row in rows:
    print(row)
#
# for item in results:
#     print(item)
#
#
# df = pd.read_sql('select * from table', con=self.client)