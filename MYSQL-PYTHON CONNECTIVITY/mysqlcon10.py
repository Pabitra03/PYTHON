import mysql.connector as c
con=c.connect(host="localhost",user="root",password="system",database="employee")
cur=con.cursor()
query="select*from grocery"
cur.execute(query)
data=cur.fetchmany(7)
for i in data:
    print(i)
    
