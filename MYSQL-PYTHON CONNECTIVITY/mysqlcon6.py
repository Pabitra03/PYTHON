import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="system",database="employee")
cur=con.cursor()
item_code=int(input("Enter the item code:-"))
item_name=input("Enter the item name:-")
query="update item set item_name='{}' where item_code={}".format(item_name,item_code)
cur.execute(query)
con.commit()
if cur.rowcount>0:
    print("Data updated succesfully...")
else:
    print("Data not found...")
