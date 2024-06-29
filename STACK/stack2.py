def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    print("Element Inserted Successfully...")
def pop(stk):
    if isEmpty(stk):
        print("Stack is empty")
    else:
        val=stk.pop()
        print("Deleted Element Is:-",val)
def peek(stk):
    if isEmpty(stk):
        print("Stack is empty")
    else:
        print("Element at top of the stack is:- ",stk[-1])
def display(stk):
    if isEmpty(stk):
        print("Stack is empty")
    else:
        a=stk[::-1]
        print("The stack elements are:-",a)        
list1=[]
while True:
    print("Menu driven program to stack implementation")
    print("1. PUSH")
    print("2. POP")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        x=int(input("Enter the element:-"))
        push(list1,x)
    elif ch==2:
        pop(list1)
    elif ch==3:
        peek(list1)
    elif ch==4:
        display(list1)
    elif ch==5:
        break
    
        
        
