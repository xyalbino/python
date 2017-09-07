import random as r

class Fish:
    def __init__(self,name):
        self.x=name

class Shark(Fish):
    def __init__(self,name):
        Fish.__init__(self,name)
        self.hungry=True

shark=Shark(25)
print(shark.hungry,shark.x)
