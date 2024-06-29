import pickle
obj1=open("file12.dat","rb")
x=pickle.load(obj1)
n=len(x)
for i in range(n):
    if x[i][0]=="Rajendra Piri":
        print(x[i])
obj1.close()
    
    
    
