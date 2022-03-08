import sqlite3 as sql

connection=sql.connect("Product.db")
result=connection.execute("select * from Product_data")

for i in result:
    print(i)
