import csv
with open("rahulambani.csv","w") as obj1:
    obj2=csv.writer(obj1)
    obj2.writerow(['Roll','Name','Marks'])
    roll=int(input("Enter the roll number:-"))
    name=input("Enter the name:-")
    marks=int(input("Enter the marks:-"))
    x=[roll,name,marks]
    obj2.writerow(x)
print("Data Inserted Successfully...")
