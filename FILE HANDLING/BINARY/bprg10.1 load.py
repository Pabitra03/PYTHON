import pickle
print("These data were stored in a binary file")
obj1=open("bfile1.dat","rb")
print(pickle.load(obj1))
obj1.close()
