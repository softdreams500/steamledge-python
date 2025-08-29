num1 = input("Enter a number: ")
num1 = int(num1)
num2 = input("Enter a number: ")
num2 = int(num2)
if num1 > num2:
    print( "num1 is greater than num2")
elif num1 < num2:
    print("num2 is greater than num1")
elif num1 == num2:
    print("both numbers are equal")
else:
    print("invalid")
    