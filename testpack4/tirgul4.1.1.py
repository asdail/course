x=int(input("Enter a 3 digit number: "))
while x<100 or x>999:
    print("Invalid Number!")
    x = int(input("Enter a 3 digit number: "))
print(x)