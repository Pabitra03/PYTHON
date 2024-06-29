obj1=open("myfile8.txt","r")
x=obj1.readlines()
for i in x:
    y=i.splitlines()
    print(y)
obj1.flush()
