a=input("Input: ")
x=""
y=""
for i in a:
    if i.isupper():
        y+=i
    else:
        x+=i
print(x+y)