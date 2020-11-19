age=int(input("Enter Age: "))
while age<0 or age>120:
    print("Invalid age!")
    age = int(input("Enter Age: "))
if 0<age<18:
    print("Child")
elif 19<age<60:
    print("Adult")
elif 61<age<120:
    print("Senior")
