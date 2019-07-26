from unit import Unit
class Player(Unit):
    
    def loot_item(self, item):
        if not self.inventory.add_to(item):
            print(f"{item.name} not looted")