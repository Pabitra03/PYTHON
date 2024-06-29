def calcFact(num):
    f=1
    i=1
    while i<=num:
        f=f*i
        i=i+1
    print("factorial of given number is-",f)
num=int(input("enter the number to find the factorial"))
calcFact(num)
    
