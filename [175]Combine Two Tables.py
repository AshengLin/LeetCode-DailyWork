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

select FirstName, LastName, City, State from Person left join Address on Person.PersonId = Address.PersonId