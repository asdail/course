class Bus:
    def __init__(self,seats=0):
        bus=[]
        self.seats=seats
        self.bus=bus
        for i in range(seats):
            bus.append([None])
        count=0
    def display(self):
        return self.bus
    def getOn(self,person):
        self.person=person
        for i in self.bus:
            if [i]==[None]:
                pass

