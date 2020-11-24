from objects.Animal.Animal import Animal
animal= Animal()
animal.name=input("Enter Name: ")
print(Animal.__str__(animal))
animal.feed+=int(input("How much do you want to feed the animal? "))
animal.eat()
print(Animal.__str__(animal))
