def pushElement(stk,x):
    stk.append(x)
    print("Data Inserted Successfully...")
    print(stk)
stack=[]
for i in range(5):
    n=int(input("Enter the value:-"))
    pushElement(stack,n)
