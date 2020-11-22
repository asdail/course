"""This is a class."""
"""A class has a name, which starts with a capital letter.
The word self refers to the name of the class.
It has functions, which include parameters that are related to the class when I refer to it with .self."""
class Car:
    def beep(self):
        print("I am a new car!",self.id, self.type, self.color, self.km, self.feul, self.tank)
    """We can also add a parameter to a function in a class, that can relate to a different function in the same class:"""
    def add_feul(self, feul):
        self.feul+=feul
        if self.feul>self.tank:
            self.feul=self.tank
    """We can add a condition to a function as well."""
    """We can use bullean logic to our advantage:"""
    def need_feul(self):
        if self.feul<5:
            return True
    """A constructor is a special method that starts before the object."""
    def __init__(self):
        print("hello")
    """The __str__ function prints the str value of a function, instead of printing the location
    of that function in memory."""
    def __str__(self):
        return f"{self.id}, {self.type}"