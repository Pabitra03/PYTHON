def displayElement(stk):
    if len(stk)==0:
        print("Stack is empty")
    else:
        index=len(stk)-1
        print("Displayed element is:-",stk[index])
    print(stk)
stack=['a','b','c','d','e']
displayElement(stack)
