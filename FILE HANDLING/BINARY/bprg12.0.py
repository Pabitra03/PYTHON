import pickle
def write():
    obj1=open("file11.dat","wb")
    list1=[]
    while True:
        nm=input("Enter the name of book:-")
        anm=input("Enter the author name:-")
        qty=int(input("Enter the quantity of book:-"))
        price=int(input("Enter the price:-"))
        total_amount=qty*price
        x=[nm,anm,qty,price,total_amount]
        list1.append(x)
        ch=input("Do you want to insert more record(y\n):-")
        if ch=="n":
            break
    pickle.dump(list1,obj1)
    obj1.close()
    print("Data Inserted Successfully...")
write()
        
