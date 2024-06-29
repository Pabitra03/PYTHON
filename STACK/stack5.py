def peekElement(stk):
    if len(stk)==0:
        print("Stack is empty")
    else:
        index=len(stk)-1
        print("peeked element is:-",stk[index])
    print(stk)
stack=[3,6,9,12,15]
peekElement(stack)
