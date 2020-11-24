from random import randint
class Lottery:
    maxpool=0
    ui=[]
    def ui(self):
        for i in range(6):
            i=randint(1,45)
            self.ui.append(i)
    def maxpool(self):
        self.maxpool=int(input("Enter maximum bet: "))
    def __init__(self):
        self.ui()
        self.maxpool()
