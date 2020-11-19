a=0
x=int(input("Insert number: "))
while x!=0:
    if x%7==0 or x%3==0:
        a+=1
        x=int(input("Insert number: "))
    else:
        x=int(input("Insert number: "))
print(a)