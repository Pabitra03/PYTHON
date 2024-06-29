import csv
def search_record():
    x=0
    roll=input("Enter the roll number to be serached:-")
    with open("details1.csv","r") as obj1:
        obj2=csv.reader(obj1)
        next(obj2)
        for i in obj2:
            if i[0]==roll:
                print(i)
                x=x+1
        if x==0:
            print("Data Not Found")
search_record()
