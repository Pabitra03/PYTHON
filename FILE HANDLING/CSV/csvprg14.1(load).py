import csv
def display():
    print("Displaying The Details...")
    with open("details2.csv","r") as obj1:
        obj2=csv.reader(obj1)
        for i in obj2:
            print(i)
display()
