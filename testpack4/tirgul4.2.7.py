sum=0
for i in range(5):
    x=int(input("Insert number: "))
    if x>0:
        sum+=x%10
    if x<0:
        sum=(((x*(-1))%10)*(-1))-sum
print(sum)

