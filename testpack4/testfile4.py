space="###################################"
grade=int(input("Enter Grade: "))
while grade<0 or grade>100:
    print("Invalid grade")
    grade = int(input("Enter Grade: "))
print(space)
###############################################
num=int(input("Enter range: "))
for i in range (1, num+1):
    print(i)