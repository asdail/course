x=input("Input: ")
a=""
for i in x:
    if i not in a:
        print(i, x.count(i))
        a+=i