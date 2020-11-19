from objects.Person import Person
dude1=Person()
dude1.name=input("Name: ")
dude1.age=int(input("Age: "))
dude1.children=int(input("Number of children: "))
dude1.info()
if dude1.hasChildren()==True:
    print(f"{dude1.name} has {dude1.children} children.")
else:
    print(f"{dude1.name} has no children.")
print(f"{dude1.name} is a {dude1.ageGroup()}.")