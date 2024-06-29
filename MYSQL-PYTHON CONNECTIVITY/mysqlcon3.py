import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="system",database="employee")
cur=con.cursor()
s_no=6
i_name="cake"
qty=5
price=10
exp_date='2005-12-13'
query="insert into grocery values({},'{}',{},{},'{}')".format(s_no,i_name,qty,price,exp_date)
cur.execute(query)
con.commit()
print('Data inserted successfully...')
   
