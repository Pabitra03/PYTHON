import pickle
def write():
    obj1=open("file11.dat","wb")
    x=int(input("How many records do you want to insert:-"))
    list1=[]
    for i in range(x):
        f=input("Enter the name of fruit:-")
        v=input("Enter the name of vegetable:-")
        df=input("Enter the name of dry fruits:-")
        y=[f,v,df]
        list1.append(y)
    pickle.dump(list1,obj1)
    obj1.close()
    print("Data Inserted Successfully...")
write()
