from unit import Unit
from item import Item
from inventory import Inventory

class Player(Unit):
    inventory = Inventory()

    def check_for_loot(self, tile):
        if issubclass(type(tile.occupant), Item):
            self.loot_item(tile.occupant)
            tile.vacate()
        else:
            print("Nothing to loot...")

    def loot_item(self, item):
        if not self.inventory.add_to(item):
            print(f"{item.name} not looted")
    
    def list_inventory(self):
        self.inventory.list_inventory()