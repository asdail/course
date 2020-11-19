space="=========================="
"""This is an example of using different kinds of variables."""
amit=1
#A whole number is called - int (intager)
shachar=2.4
#A number with a decimal is called - float
###
print(space)
###
"""We can switch between different kinds of variables in the middle of the string."""
amit=2.6
print(amit)
amit=3
print(amit)
amit="hello"
#text as a variable is called - string
print(amit)
###
print(space)
###
"""We can do mathematical functions using int or float variables (numerical variables) as well."""
amit=1
shachar=2.5
print(amit*shachar)
print(amit+shachar)
print(shachar-amit)
print(shachar/amit)
#If we want to use parenthesis in an eqasion, we need to put the whole print function in parenthesis first.
print(shachar/(amit+shachar))
###
print(space)
###
"""We can create a new numerical variable by defining it as the sum of two or more numerical variables."""
shetula=amit+shachar
print(shetula)
###
print(space)
###
"""We can also add text to a command line with a numerical variable in the print command."""
print(amit,"plus",shachar,"equals",shetula, ",as you can clearly see.")
#adding a comma adds a space between characters.
"""If we want to convert a numerical variable to a text variable, we can do so by using the str command."""
print(amit,"plus",shachar,"equals" +str(shetula),",as you can clearly see.")
"""We can also define numerical variables in a sring line using the % function."""
# %d = int
# %f = float
# %.xf = float with x decimal numbers behind it
# %s = string
print("amit is %d and shachar is %f" % (amit,shachar))
"""IMPORTANT NOTE!
In the 1st and 3rd method, the variable stays a numerical variable (int/float).
In the 2nd method, the int or float variable is CONVERTED into a string variable.
This is used mainly in automation, when I want to print a numerical variable into the client I'm testing,
but the client only accepts an str variable."""
###
"""The easiest way to enter a numerical variable in a string line is to add the letter f (formatting) 
in the beginning of a print command. This tells the software to print whatever numerical variable 
that's inside the curly brackets {} without commas and complications."""
print(f"{amit} plus {shachar} equals {shetula}, as you can clearly see.")
print(f"{amit} plus {shachar} equals {amit+shachar}, as you can clearly see.")
###
print(space)
###
d=3
m=11
y=2020
"""If I want something to go one line down, I need to add \n before the function.
I can go down multiple lines by writing \n multiple times."""
print(f"The date today is: \n{d}/{m}/{y}")
###
print(space)
###
"""If I want to divide two numerical variables and get a whole number, I use //."""
a=9
b=2
print(a/b)
print(a//b)
"""If I want to calculate the leftover of a mathematical function, I use % (modulu)."""
print(a%b)
#We'll use this function to know if the result of the division of two nnumbers is a whole number.
#If the result is a whole number, runnumg the function will result in 0.
print(10%b)
#if I want to find one number from a three-digit number, this is how:
num=876
print(num)
#Right Digit
print(num%10)
#Middle Digit
print(num%100//10)
print(num//10%10) #Second from the right *consistently*
#Left Digit
print(num//100)
