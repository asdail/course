d1={1:10,2:20,3:30,4:40}
d2={}
for i in d1:
    d2.update({d1[i]:i})
    #d2[d1[i]]=i
print(d2)