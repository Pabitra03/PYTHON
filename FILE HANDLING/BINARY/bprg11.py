import pickle
obj1=open("file10.dat","wb")
list1=[]
for i in range(3):
    roll=int(input("Enter the roll number:-"))
    nm=input("Enter the name of student:-")
    gender=input("Enter the gender:-")
    age=int(input("Enter the age:-"))
    x=[roll,nm,gender,age]
    list1.append(x)
pickle.dump(list1,obj1)
obj1.close()
print("Data Inserted Successfully... ")
    
    
