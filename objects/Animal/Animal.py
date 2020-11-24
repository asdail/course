class Animal:
    feed=0
    hunger=float(0)
    energy=float(0)
    name=""
    def __init__(self):
        self.hunger+=5
        self.energy+=5
    def __str__(self):
        return f"Your animal:\nAnimal Name: {self.name}\nHunger Level: {self.hunger}\nEnergy Level: {self.energy}"
    def eat(self):
        self.hunger=self.hunger-self.feed/50
        self.energy=self.energy-self.feed/100
    def full(self):
        while self.hunger<0:
                self.hunger=0
                print("I'm full!")