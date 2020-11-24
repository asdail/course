from objects.Animal.Animal2 import Animal
name=input("What's your animals name? ")
hyena=Animal(name)
print(hyena.__str__())
print("You can feed your animal or play with it\n\
If you want to play with the animal, write 'Play'.\n\
If you want to feed the animal, write 'Eat'.\n\
If you want to exit the program, write 'Exit'.")

action=input(f"So, What do you want {hyena.name} to do? ")
while action is not "Exit":
    if action=="Eat":
        food=int(input(f"How much do you want to feed {hyena.name}? (in grams) "))
        hyena.eat(food)
        action = input(f"So, What do you want {hyena.name} to do? ")

    if action=="Play":
        playtime=int(input(f"For how many minutes do you want to play with {hyena.name}? "))
        hyena.play(playtime)
        action = input(f"So, What do you want {hyena.name} to do? ")

    if action=="Exit":
        break
