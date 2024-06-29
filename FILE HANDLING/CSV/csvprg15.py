import csv
def create():
    with open("details1.csv","w",newline="") as obj1:
        obj2=csv.writer(obj1)
        obj2.writerow(["Roll","Name","Marks"])
        while True:
            roll=int(input("Enter the roll number:-"))
            name=input("Enter the name:-")
            marks=int(input("Enter the marks:-"))
            record=[roll,name,marks]
            obj2.writerow(record)
            ch=input("Do you want to enter more records(y/n):-")
            if ch=='n':
                break
create()
print("Data Inserted Successfully...")
def display():
    with open("details1.csv","r") as obj1:
        obj2=csv.reader(obj1)
        for i in obj2:
            print(i)
display()
