import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="system",database="employee")
if con.is_connected():
    print("successfully connected...")
else:
    print("some connectivity problem....")
