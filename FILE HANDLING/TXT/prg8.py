obj1=open("myfile8.txt","a")
for i in range(2):
    roll=int(input("Enter the roll number"))
    nm=input("Enter the name of student")
    marks=int(input("Enter the marks"))
    record=str(roll) +"\t" +nm + "\t" +str(marks)+"\n"
    obj1.write(record)
obj1.flush()
print("Data Inserted Successfully")
    
