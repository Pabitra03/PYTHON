import pickle
obj1=open("file12.dat","wb")
n=int(input("Enter The Number Of The Students"))
list1=[]
for i in range(n):
    name=input("Enter the name:-")
    roll=int(input("Enter the roll number:-"))
    cla=int(input("Enter the class:-"))
    x=[name,roll,cla]
    list1.append(x)
pickle.dump(list1,obj1)
obj1.close()
print("Data Inserted Successfully...")
