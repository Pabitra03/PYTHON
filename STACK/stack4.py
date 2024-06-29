def popElement(stk):
    if len(stk)==0:
        print("stack is empty")
    else:
        x=stk.pop()
        print("The poped element is:-",x)
    print(stk)
stack=[10,20,30,40,50]
popElement(stack)
