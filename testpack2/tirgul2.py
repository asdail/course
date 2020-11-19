space="============================"
#1.
print("1.")
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=a+b
#c/=2
if c%2!=0:
    print("Invalid")
else:
    print("Valid")
print(space)
####################################
#2.
print("2.")
x=int(input("Enter a number: "))
if 99<x<1000:
    print(x)
    print("Great!")
else:
    print(x)
    print("INVALID.")
print(space)
####################################
#3.
print("3.")
age=int(input("How old are you? "))
if 0<age<18:
    print("You are a child.")
if 19<age<60:
    print("You are an adult.")
if 61<age<120:
    print("You are a senior.")
print(space)
####################################
#4.
print(".4")
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=a-b
if c>=0:
    print(c)
else:
    print(b-a)
print(space)
####################################
#5.
print("5.")
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if a%2==0 and b%2==0:
    print(f"{a}+{b}={a+b}")
else:
    print(f"{a}*{b}={a*b}")
print(space)
####################################
#6.
print("6.")
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
if a+b==10:
    print("Great!")
else:
    print("Nah")
print(space)
####################################
#7.
print("7.")
print("What's the date today?")
d=int(input("Day: "))
m=int(input("Month: "))
y=int(input("Year: "))
if 1<=d<=31 and 1<=m<=12 and 1950<=y<=2020:
    print(f"{d}/{m}/{y%100}")
#else:
#    print("Invalid Date")
elif d<1 or d>31:
        print("Invalid day")
elif m<1 or m>12:
        print("Invalid month")
elif y<1950 or y>2020:
        print("Invalid Year")