import csv
def search():
    x=0
    roll=input("Enter the roll number to be searched:-")
    with open("details2.csv","r") as obj1:
        obj2=csv.reader(obj1)
        next(obj2)
        for i in obj2:
           if i[1]==roll:
               print(i)
               x=x+1
        if x==0:
            print("Data not found")
search()
