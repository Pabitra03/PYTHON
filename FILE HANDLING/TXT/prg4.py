obj1=open("myfile4.txt","w")
for i in range(3):
    roll=int(input("Enter The Roll Number"))
    nm=input("Enter the name of students\n")
    marks=int(input("Enter The Marks"))
    obj1.write(str(roll) + "\t" + nm + " \t" + str(marks))
    obj1.write('\n')
obj1.close()
print("Data Inserted Successfully...")
