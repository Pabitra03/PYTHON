import pickle
print("These data were stored in a binary file")
obj1=open("file11.dat","rb")
record=pickle.load(obj1)
if record[0][0]=="python":
    print(record[0])
obj1.close()
