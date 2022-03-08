import sqlite3 as sql

connection=sql.connect("Product.db")

getProductCode=input("Enter the Product code : ")


result=connection.execute("select * from Product_data WHERE Product_Code ="+getProductCode)


for i in result:
   print(i)