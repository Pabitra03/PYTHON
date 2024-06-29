obj1=open("myfile6.txt","w")
list1=[]
for i in range(3):
    nm=input("Enter the name of students\n")
    list1.append(nm)
    obj1.writelines(list1)
obj1.close()
print("Data Inserted Successfully...")
