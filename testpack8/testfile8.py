space="################################################################################################################"
"""This is a function that takes a list and creates a new list where the values from the first list are multiplied by 2."""
def mult_listby2(list):
    list2=[]
    for i in list1:
        list2.append(i*2)
    return list2
list1=[10,20,30,40]
print(mult_listby2(list1))
"""We can add more actions to a function by inserting a number of parameters in the brackets and using them in the function:"""
def mult_list(list,num):
    list2=[]
    for i in list:
        list2.append(i*num)
    return list2
print(mult_list(list1,5))
"""There don't have to be parameters in a function:"""
from random import randint
def get_random_numbers():
    list2=[randint(1,100) for i in range (10)]
    return list2
x=print(get_random_numbers())

"""We can add optional parameters to a function using **:"""
def print_details(id,**keywords):
    print(keywords)
    print(id)
    for i in keywords:
        print(i,keywords[i])
print_details(123,name='Gil',age='20')
"""We can add optional paramaters as a tuple using *:"""
def int_sum(a,b,*args):
    sum=a+b
    for i in args:
        sum+=i
    print(sum)
    print(args)
int_sum(1,2,3,4,5,6)
###
def delete_from_list_and_add(list1,loc=-1,*items):
    """A function that recieves a list and location (default=-1) and deletes that item from the list in the location
    recieved."""
    list1.remove(list1[loc])
    list_items=list(items)
    list1+=list_items
    return list1
list1=[1,2,3,4]
new_list=delete_from_list_and_add(list1,0,10,20,30)
print(new_list)
"""We can define a parameter as a global parameter by using the global function."""
def f1():
    global a
    a+=1
a=5
f1()
print(a)