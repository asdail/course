a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
while a%2==0 and b%2==0:
    print(a+b)
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
if not a%2==0 or b%2==0:
    print(a*b)