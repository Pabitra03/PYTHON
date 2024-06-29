num1 = int(input("Enter your marks:-"))

if num1>=90:
    grade = "Ex"
elif num1>=80:
    grade = "A"
elif num1>=70:
    grade = "B"
elif num1>=60:
    grade = "c"
elif num1>=50:
    grade = "D"
else:
    grade = "F"
print("Your grade is " + grade)