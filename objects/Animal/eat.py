from objects.Animal.hunger import hunger
from objects.Animal.energy import energy
def eat(self):
    return self.feed==int(input("How much do you want to feed the animal? "))
def hungerReduced(self):
    return self.feed/50
def energyReduced(self):
    return self.feed/100