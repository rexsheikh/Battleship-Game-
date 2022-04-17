class Watercraft():
    def __init__(self,length,name, health):
        self.length = length
        self.health = health
        self.name = name 
        self.coords = []
    

    def decrement_health(self):
        self.health -= 1

    def display_health(self):
        print(f"{self.name} Health : {self.health}/{self.length}")

    def stringify_coords(self,coords):
        self.str_coords = ''.join(self.coords)
        return self.str_coords
    
   


