a=input("Input #1 :")
b=input("Input #2: ")
c=len(a)+len(b)
d=a[0]
for i in range(1,c):
    #if len(a)==len(b):
    if i>len(a) or i>len(b):
        d+=c[i:]
    else:
        d+=b[-i]+a[i]
print(d)
