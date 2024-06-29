n=int(input("How many record do you want to enter"))
obj1=open("myfile7.txt","w")
list1=[]
for i in range(n):
    nm=input("Enter the name of students")
    list1.append(nm +'\n')
    obj1.writelines(list1)
obj1.close()
print("Data Inserted Successfully...")
