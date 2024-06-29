import csv
def create():
    with open("details2.csv","w",newline="") as obj1:
        obj2=csv.writer(obj1)
        obj2.writerow(["Admn","Roll","Class","Name"])
        while True:
            admn=int(input("Enter the admission number:-"))
            roll=int(input("Enter the roll number:-"))
            cls=input("Enter the class:-")
            name=input("Enter the name:-")
            x=[admn,roll,cls,name]
            obj2.writerow(x)
            ch=input("Do you want to enter more records (Y/N):-")
            if ch=='n':
                break
create()
print("Data Inserted Successfully...")
