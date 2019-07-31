from point import Point

class Unit(object):
    #Class variables
    location = None
    status = "Alive"

    def __init__(self, name="New Unit", hp=100):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def use_item(self, item):
        item.use(self)
    
    def take_damage(self, damage):
        if self.status == "Alive":
            self.hp - damage
            if self.hp < 0:
                self.status = "Dead"
    
    def heal(self, healing):
        if self.status == "Alive":
            self.hp + healing
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        else:
            print(f"Unit {self.name} is already dead")
    
    def set_location(self, x, y):
            self.location = Point(x, y)