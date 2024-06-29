import pickle
print("These data were stored in a binary file")
obj1=open("file11.dat","rb")
x=1
r=" "
while True:
    r=pickle.load(obj1)
    print(r)
    x=x+1
obj1.close()
    
    
