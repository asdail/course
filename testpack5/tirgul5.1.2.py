from random import *
user=input("Enter Username: ")
user=str(user)
a=len(user)
pw=""
for i in range(6):
    b=randint(0,a)
    pw+=user[b]
print(pw)