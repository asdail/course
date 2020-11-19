x=int(input("Insert grade:"))
#Highest Grade:
high=0
#Average:
a=0
#Total:
b=0
#Stepper:
s=0

while 0<x<101:

    if x>high:
        high=x
    if x>=101:
        break
    s+=1
    b+=x
    x=int(input("Insert grade:"))
a=b/s
print(f"Highest Grade: {high}\n\
Average Grade: {a}\n\
Gap between highest grade and average: {high-a}")
