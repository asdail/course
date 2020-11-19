x=input("Input: ")
#a=0
b=""
if x[0]:
    b=x[0]
    #a+=1
if b in x[1:]:
    x=b+x.replace(b,"$")[1:]
print(x)