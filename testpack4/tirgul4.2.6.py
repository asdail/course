a=0
b=0
c=0
d=0
x=int(input("Enter Grade: "))
while 0<x<100:
    if x>60:
        a+=x
        b+=1
    else:
        c+=x
        d+=1
    x = int(input("Enter Grade: "))
print(a)
print(c)
print(a/b)
print(c/d)
