tup1=(1,2,3,4,5)
x=int(input("Put in a number between 1 to 5: "))
while 1>x>5:
    print("Invalid number.")
    x=int(input("Put in a number between 1 to 5: "))
for i in tup1:
    if i==x:
        print(tup1.count(x))