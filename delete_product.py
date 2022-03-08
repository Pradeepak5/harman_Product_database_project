import sqlite3 as sql

connection=sql.connect("Product.db")

getProductCode=input("Enter the product code :")

connection.execute("delete from Product_data where Product_Code="+getProductCode)

print("data deleted successfully")

result=connection.execute("select * from Product_data")

for i in result:
    print(i)