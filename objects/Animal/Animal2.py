class Animal:

    def __init__(self,name,energy=5,hunger=5):
        self.name=name
        self.energy=float(energy)
        self.hunger=float(hunger)

    def __str__(self):
        return f"Your animal:\n\
        Name:{self.name}\n\
        Current Energy Level:{self.energy}\n\
        Current Hunger Level:{self.hunger}"

    def eat(self,food):
        self.food=int(food)
        if self.hunger-self.food/50<0:
            self.food=self.hunger*50
            print("The animal isn't hungry anymore, and didn't finish it's food.")
            self.hunger=0.0
            self.energy-=self.food/100
        elif self.energy-self.food/100<0:
            self.energy=0.0
            self.hunger-=self.food/50
        else:
            self.hunger-=self.food/50
            self.energy-=self.food/100
        print(self.__str__())

    def play(self, playtime):
        self.playtime=int(playtime)
        if self.energy-(self.playtime/10)*2<0:
            self.playtime=(self.energy*10)/2
            self.energy=0.0
            self.hunger+=(self.playtime/10)*2
        elif self.hunger+(self.playtime/10)*2>10:
            self.hunger=10
            self.energy-= (self.playtime/10)*2
        else:
            self.energy-= (self.playtime/10)*2
            self.hunger+= (self.playtime/10)*2
        print(self.__str__())

    #def rest(self,resttime):
        #self.resttime=int(resttime)



