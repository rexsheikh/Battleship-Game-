class Watercraft():
    def __init__(self,length,name, health):
        self.length = length
        self.health = health
        self.name = name 
        self.coords = []

    def decrement_health(self):
        self.length -= 1

    def display_health(self):
        print(f"{self.name} Health : {self.length}/{self.health}")
    
   


