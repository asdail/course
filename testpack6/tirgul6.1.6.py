list1=[1,2,3,4,5,6,7,8,9,10]
#a.
list2=list1[-3:]
print(list2)
#b.
print(list1[::-1])
#c.
print(list1[1::2])
#d.
list2=list1[::2]
print(list2)
#e.
a=int(input("Insert number: "))
b=int(input("Insert number: "))
list1[4:6]=[a,b]
c=int(input("Insert number: "))
list1.append(c) #list1+=[c]
print(list1)
#f.
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for i in list1:
    list2.append(i*2)
print(list2)
#g.
list2=[list1[0],list1[-1]]
print(list2)