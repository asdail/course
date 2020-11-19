a=input("Enter 1st word: ")
b=input("Enter 2nd word: ")
count=0
x=len(a)
for i in range(x):
    if a[i]in b:
        count+=1
print(count)
