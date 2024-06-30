obj1 = open("myfile.txt","w")

for i in range(3):
    nm = input("Enter the name:-")
    roll = int(input("Enter the roll number:-"))
    marks = int(input("Enter the marks:-"))
    x = nm + '\t' + str(roll) + '\t' + str(marks) + '\n'
    obj1.write(x)
obj1.close()
print("Data Inserted Successfully...")
