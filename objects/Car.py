class Car:
    def beep(self):
        print("I am a new car!", self.id, self.type, self.color, self.km, self.feul, self.tank)
    def add_feul(self,feul):
        self.feul+=feul
        if self.feul>self.tank:
            self.feul=self.tank
    def need_feul(self):
        if self.feul<5:
            return True