space="=========================="
"""We can let the user input his own result. The input will always come out as string."""
x=input("Enter Age: ")
"""There are 2 ways to translate an str input into int:"""
#1: After the input command
x=input("Enter Age: ")
x=int(x)
#2: Before the input command
x=int(input("Enter Age: "))
print(space)
"""Instead of writing the same variable multiple times to print it multiple times or in a mathematical
equasion, we can use +=, -=, *=, /= and more."""
number_of_students=20
print(number_of_students)
number_of_students+=5
print(number_of_students)
print(space)
"""We can import functions that don't exist in the basic code."""
from random import randint
#We can also import a whole package.
from random import *
#We can also import a whole package just using import, but we'll have to put an intro to the
#package before we use a function.
import random
x=input("Pick a bottom number: ")
x=int(x)
y=input("Pick a top number: ")
y=int(y)
print(random.randrange(x,y))
from random import *
a=int(input("Enter low number: "))
b=int(input("Enter high number: "))
#randint - Randomize an integer in a given range
print(randint(a,b))
#print(random()) - Prints a random fraction
print(random())
print(space)
"""We can put up conditions for a certain functiom"""
x=int(input("Enter a number: "))
if x>=0:
    print("Positive")
else:
    print("Negative")
"""We can add multiple outputs to a condition"""
x=int(input("Enter a number: "))
if x>=0:
    print("Positive")
else:
    print("Negative")
    x+=5
    print(x)
print(space)
"""We can check a value between certain numbers"""
grade=int(input("Enter grade: "))
if 0<=grade<=100:
    print("Valid grade")
else:
    print("Invalid Grade")
#We can do this with the or command as well
grade=int(input("Enter a grade: "))
if grade>=0 or grade >=100:
    print("Valid Grade")
else:
    print("Invalid Grade")
print(space)
#We can add multiple conditions to a statement
grade=int(input("Enter Grade: "))
name=input("Enter Name: ")
if name=="Amit" or name=="Shachar" and grade >=60:
    print("Passed!")
else:
    print("Failed")
"""If the user dosen't input any string, we can produce an error message instead of the whole
program crashing"""
a=input("Enter Amount: ")
if a=="":
    print("No input.")
print(space)
"""If we want to condition a condition, we can produce a nested if."""
num=int(input("Enter number: "))
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")
#We can get the same result by using elif
num=int(input("Enter number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")