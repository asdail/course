a=input("Input: ")
b=""
#b - First word
c=""
#c - Second word
y=True
#y - bullean variable - like a switch
wa=""
wb=""
print(f"Initial Input: {a}")
for i in a:
    if i!=" " and y==True:
        b+=i
    else:
        y=False
    if y==False and i!=" ":
        c+=i
wa=b[:2]
wb=c[:2]
print(b.replace(wa,wb), c.replace(wb,wa))