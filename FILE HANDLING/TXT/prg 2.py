obj1=open("myfile2.txt","w")
for i in range(1,6):
    nm=input("Enter the name of student\n")
    obj1.write(nm)
    obj1.write('\n')
obj1.close()
print("Data Inserted Successfully...")
