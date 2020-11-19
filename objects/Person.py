class Person():
    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("No. of children:",self.children)
    def hasChildren(self):
        if self.children==0:
            return False
        else:
            return True
    def ageGroup(self):
        if 0<=self.age<18:
            return "Child"
        elif 19<self.age<60:
            return "Adult"
        elif 61<self.age<120:
            return "Senior"