import mysql.connector as c
con=c.connect(host="localhost",user="root",password="system",database="employee")
cur=con.cursor()
item_code=int(input("Enter the item code:-"))
query="delete from item where item_Code={}".format(item_code)
cur.execute(query)
con.commit()
if cur.rowcount>0:
    print('Data updated successfully...')
else:
    print("Data not found..")
