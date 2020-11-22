class Animal:
    def __init__(self):
        self.hunger=0
        self.energy=0
        self.feed=0
        self.hunger=float(self.hunger)
        self.energy=float(self.energy)
        self.name=""
        self.hunger+=5
        self.energy+=5
    def __str__(self):
        return f"Your animal:\nAnimal Name: {self.name}\nHunger Level: {self.hunger}\nEnergy Level: {self.energy}"
    def eat(self):
        return self.feed==int(input("How much do you want to feed the animal? "))
    def feedResult(self):
        self.hunger-=self.feed/50
        self.energy-=self.feed/100
