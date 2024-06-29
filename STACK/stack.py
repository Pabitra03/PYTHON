def pushElement(a,val):
    a.append(val)
    print("Items Inserted Successfully...")
def popElement(a):
    x=a.pop()
    print("Deleted Element Is:-",x)
def peekElement(a):
    index=len(a)-1
    print("Top Element Or Peeked Element Is:-",a[index])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])
stack=[]
while True:
    print("Stack operations")
    print("1. PUSH")
    print("2. POP")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        value=int(input("Enter the items to PUSH"))
        pushElement(stack,value)
    elif ch==2:
        if len(stack)==0:
            print("Stack is empty or item cannot be deleted")
        else:
            popElement(stack)
    elif ch==3:
        if len(stack)==0:
            print("Stack is empty or top element can't be displayed")
        else:
            peekElement(stack)
    elif ch==4:1
        if len(stack)==0:
            print("Stack is empty or there is no element in stack")
        else:
            display(stack)            
    elif ch==5:
        break
    
