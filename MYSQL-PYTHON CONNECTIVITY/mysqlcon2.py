import mysql.connector as c
con=c.connect(host="localhost",user="root",password="system",database="employee")
if con.is_connected():
    cur=con.cursor()
    while True:
        s_no=int(input("Enter the serial number:-"))
        i_name=input("Enter the item name:-")
        qty=int(input("Enter the qty:-"))
        price=eval(input("Enter the price:-"))
        exp_date=eval(input("Enter the date:-"))
        query="insert into grocery values({},'{}',{},{},'{}')".format(s_no,i_name,qty,price,exp_date)
        cur.execute(query)
        con.commit()
        print("Data inserted successfully...")
        x=input("Enter your choice(y/n)")
        if x==n:
            break
