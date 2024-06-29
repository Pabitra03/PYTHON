import mysql.connector as c
con=c.connect(host="localhost",user="root",password="system",database="employee")
cur=con.cursor()
query="update grocery set i_name='wheat' where s_no=5" 
cur.execute(query)
con.commit()
print('Data updated successfully...')
   
