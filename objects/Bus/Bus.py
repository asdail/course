class Bus:
    person=[]
    count=sum(person)
    def __init__(self,seats=0):
        self.seats=int(input("Number of seats:"))