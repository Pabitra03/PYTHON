obj1=open("myfile9.txt","w+")
x=input("Enter the contents to be written in the file:")
obj1.write(x)
print("Reading the content of the file...")
for i in obj1:
    print(i)
obj1.flush()
