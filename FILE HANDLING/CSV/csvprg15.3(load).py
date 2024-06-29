import csv
def search():
    max=0
    x=str(max)
    with open("details1.csv","r") as obj1:
        obj2=csv.reader(obj1)
        next(obj2)
        for i in obj2:
            if i[2]>x:
                roll=i[0]
                name=i[1]
                marks=i[2]
                x=i[2]
                print(roll,name,marks)
search()
