x=int(input("Enter Grade: "))
grades=[]
passed=0
fail=0
while x!=611:
    grades.append(x)
    if x>60:
        print("Passed")
    else:
        print("Failed")
    x=int(input("Enter Grade: "))
print(grades)
for i in grades:
    if i>=60:
        passed+=1
    else:
        fail+=1
print(f"{passed} students passed the test.\n{fail} students failed the test.")