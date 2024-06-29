import csv
def search():
    with open("details2.csv","r") as obj1:
        obj2=csv.reader(obj1)
        for i in obj2:
            if (i[0]<'300'):
                print(i)
search()
