a=0
b=0
x=int(input("Enter Grade: "))
while 0<x<100:
    if x>60:
        a+=x
        b+=1
    x = int(input("Enter Grade: "))
print(a)
print(a/b)
