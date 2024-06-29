import csv
def search():
    with open("details1.csv","r") as obj1:
        obj2=csv.reader(obj1)
        next(obj2)
        for i in obj2:
            if i[2]>='70':
                print(i)
search()
