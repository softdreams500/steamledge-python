char = input("Enter a single character: ")
if len(char) != 1:
    print("Please enter only one character")
if char.isupper():
    print("Uppercase")
elif char.islower():
    print("lowercase")
else:
    print("Not a Letter")
    
