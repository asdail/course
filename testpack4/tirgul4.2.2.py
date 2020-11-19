i=0
sum=0
y=0
for i in range(6):
    x=int(input("Enter number: "))
    if x%2==0:
        sum+=x
        y+=1
print(y)
print(sum/y)