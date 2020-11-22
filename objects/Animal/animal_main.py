from objects.Animal.Animal import Animal
animal= Animal()
animal.name=input("Enter Name: ")
print(Animal.__str__(animal))
animal.eat()
animal.feedResult()
print(Animal.__str__(animal))
