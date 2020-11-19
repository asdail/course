space="##################################"
"""This is called a list."""
numbers=[1,2,3,4]
print(numbers)
#List is a type as well.
print(type(numbers))
"""A list can include a mix of every data type - int, float, str.."""
numbers=[1,2,"abc",4.67,"$tr"]
print(numbers)
"""A variable in a list updates only when I tell it to."""
x=20
numbers=[x,1,2]
x=0
print(numbers)
#You can change a value in a list like this, as long as I don't replace it with str:
numbers[0]=3
print(numbers)
numbers=[3,1,2,x,"abc"]
#If we want to switch a string index with string, this is how you do it:
numbers[4]=numbers[4].replace("abc","cba")
print(numbers)
"""We can also count the amount of items in a list:"""
print(len(numbers))
"""We can input our own value in a list:"""
numbers[4]=input("Enter value:")
print(numbers)
print(space)
##########################################################################
"""We can add values into a list:"""
list1=[]
grade=int(input("Enter Grade: "))
list1.append(grade)
print(list1)
#Append adds a value to the end of a list.
"""We can do so by adding a value to a new list as well:"""
list1=[]
grade=int(input("Enter Grade: "))
list1+=[grade]
print(list1)
print(space)
##########################################################################
"""This works best in a loop:"""
from random import randint
list1=[]
for i in range(10):
    list1.append(randint(1,100))
print(list1)
"""We can multiply a list and it creates a new list with the new values:"""
print(list1*3)
"""We can remove an item from a list:"""
list2=[1,2,3,4,5,"abc",6,"abc"]
list2.remove(1)
print(list2)
#The remove function only treats the firt occurance of a value in a list.
list2.remove("abc")
print(list2)
"""If I want to slice a range of values in a list, we can do it the same as any other value:"""
print(list2[2:5])
list2[2:5]=[100,200,300,400,500]
print(list2)
"""We can sum the numbers in a list, find out the smallest number or find the biggest number."""
list1=[1,2,3,4,5,6,7,8,9,10]
print(sum(list1))
print(min(list1))
print(max(list1))
#We can use the min and max functions with a sreing list as well. The function will work alphabetically.
list1=["a","b","xyz","aa"]
print(min(list1))
print(max(list1))
print(space)
"""This is the easiest way to add items to a list:"""
list1=[1,2,3,4,5,6,7,8,9,10]
list2=[]
for i in list1:
    list2+=[i*2]
print(list1)
print(list2)
"""We can replace values in a whole list:"""
for i in range(len(list1)):
    list1[i]*=2
print(list1)
"""We can remove a certain item (not an index) in a list:"""
list1=[1,2,3,4,5,6,7,8,9,10]
list1.remove(5)
print(list1)
"""If I don't know if an item is in a list and I don't want an error while running the program, I can pu in a condition:"""
if 5 in list1:
    list1.remove(5)
else:
    print("5 dosen't exist")
print(space)
"""The pop function removes a certain index from a list, but I can save the number that it removed in a variable."""
list1=[1,2,3,4,5,6,7]
#If I don't put an index number in the brackets, it will automatically remove the last index in the list.
x=list1.pop()
print(x)
print(list1)
"""The index function will give me back the index of a certain item:"""
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1.index(5))
#We can also include a range for the function to look in:
print(list1.index(5,2,6))
print(list1.index(6,0))
#We can do the same thing with string using the find function:
x="12345789876"
print(x.find("56",8))
print(space)
"""If I want to print a list backwards, I create a loop:"""
list1=[1,2,3,4,5,6,7,8,9,10]
for i in range (len(list1)-1,-1,-1):
    print(i)
#We can do it easier by using the reverse function;
list1.reverse()
print(list1)
#or:
list2=list1[::-1]
print(list2)
"""We can use the sort function, that will sort a list in ascending order:"""
list1.sort()
print(list1)
#We can sort them in reverse using a bulean sentence:
list1.sort(reverse=True)
print(list1)
print(space)
"""We can copy a list in it's current state to a different list:"""
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1.copy()
list2.append(11)
print(list1)
print(space)
############################
"""We can create a whole new list in a loop without creating an empty list before it"""
list1=[i for i in range(10)]
print(list1)
list1=[i*2 for i in range(10)]
print(list1)
print(space)
#############################
"""We can split a string sentence into single items, using the split function"""
word=input("Enter a sentence: ")
list1=word.split()
#The default string item that seperates the words is space, but you can change it into anything else
print(list1)
"""The opposite of slpit is join` if I want to create a string using items from a list, I use join:"""
list1=["I","Love","Python"]
str1=" ".join(list1)
print(str1)
