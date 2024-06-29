n1 = int(input("Enter the number 1:-"))
n2 = int(input("Enter the number 2:-"))
n3 = int(input("Enter the number 3:-"))

if(n1<33 or n2<33 or n3<33):
    print("You are fail")
elif(n1+n2+n3)/3 <40:
    print("You are also fail")
else:
    print("You are pass")