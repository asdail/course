space="========================================"
#1.
print("1.")
x=int(input("Enter a number: "))
if x%2==0:
    print("Great!")
else:
    print("Invalid.")
print(space)
################################################
#2.
print("2.")
a=int(input("Number #1: "))
b=int(input("Number #2: "))
c=int(input("Number #3: "))
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
print(space)
################################################
pc=input("How many computers did you fix today? ")
if pc=="" or pc==str(pc):
    pc=15
else:
    pc=int(pc)
print(f"You have {pc*2} computers to take care of tomorrow.")
