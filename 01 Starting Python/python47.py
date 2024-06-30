a = int(input("Enter the number:-"))
for i in range(2,a):
    if(a%i==0):
        print("The number is prime")  
    else:
        print("The number is not prime")