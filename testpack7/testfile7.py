space="###################################################"
"""This is a tuple."""
tup1=(1,2,3)
print(tup1)
"""In a tuple, you can't change the value of an index by inserting a value. You can only add values."""
tup1+=(4,5,6)
print(tup1)
#If I only want to add one value to a tuple, this is how:
tup1+=(7,)
print(tup1)
"""In a tuple, you can combine all kinds of types"""
list1=[1,2,3,4,5]
tup1=(list1,6,7,8,"Nine","Ten!")
print(tup1)
"""Defining a tuple can be done without brackets as well."""
tup1=1,2,3,4
print(tup1)
"""We can find an index in a tuple by using brackets:"""
print(tup1[0])
"""A variable can also be a tuple. we can equalise a number of variables with a number of inputs:"""
a,b=5,6
print(a,b)
#We can also switch variables in a tuple:
a,b=b,a
print(a,b)
"""The only way we can change or remove a value from a tuple is if we convert the tuple to a list:"""
list1=list(tup1)
print(tup1)
tup1=list1[1]=20
print(tup1)
print(list1)
tup1=tuple(list1)
print(tup1)
print(space)
#############################################################
"""This is a dictionary."""
d1={1:10,2:20,3:30,4:40}
print(d1)
"""In a list, instead of indexes there are keys. You can use any key you want, even string."""
d1={"int":"Intager","float":"Float","str":"String"}
print(d1["int"])
"""We can change a value in a dictionary, but we can't change a key."""
d1["int"]="InTaGeR"
print(d1["int"])
"""Dictionary in a for loop prints out the keys:"""
for i in d1:
    print(i)
"""A value can have anything in it. A key can have anything BUT lists."""
"""I can speprate the values and keys into lists."""
print(list(d1.keys()))
print(list(d1.values()))
"""Finding a key through a value:"""
d1={1:10,2:20,3:30,4:40,5:50,6:60,7:70,8:80,9:90}
x=40
for i in d1:
    if d1[i]==x:
        print("The key is",i)
"""We can add or update values in a dictionary with the update feature:"""
d1.update({10:100,11:110})
print(d1)
"""We can convert a dictionary to a list, tuple or a list of tuples which contain a key and its value"""
print(list(d1))
print(tuple(d1))
print(d1.items())
"""We can find a key through a value in a for loop with the items function:"""
for i in d1.items():
    if i[1]==70:
        print(i[0])
"""There are two ways to delete a dictionary:"""
d1.clear()
#clear dosen't delete a dictionary, but it empties it.
d1={1:10}
del d1
print(space)
#############################################################
"""This is a set."""
set1={1,2,3}
"""A set is a series of values. There can't be two identical values in a set, so every value is one of a kind.
There's also no order to a set."""
"""This is an empty set."""
set2=set()
"""You can add values to a ste:"""
set1.add(4)
print(set1)
"""We can use sets to delete doubles in a list:"""
list1=[1,2,3,4,4,5,5,3,2,7,6,5,5]
set1=set(list1)
list1=list(set1)
print(list1)
"""We can"""