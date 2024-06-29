import pickle
list1=[1,"B2gang","male",18]
obj1=open("bfile1.dat","wb")
pickle.dump(list1,obj1)
obj1.close()
print("Data Inserted Successfully...")
