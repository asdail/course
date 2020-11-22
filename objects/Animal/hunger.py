from objects.Animal.eat import hungerReduced
def hunger(self):
    self.hunger=float(0<=self.hunger<=10)
    self.hunger-=hungerReduced()