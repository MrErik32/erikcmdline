class Inventory:
    #Class Variables
    inventory = []

    def __init__(self, size=6):
        self.size = size
    
    def add_to(self, item):
        if len(self.inventory) < self.size:
            self.inventory.append(item)
            return True
        else:
            return False

    def remove_from(self, item_name):
        if self.inventory.count(item_name) != 0:
            self.inventory.remove(item_name)
            return True
        else:
            print("Item doesn't exist")
            return False

    def list_inventory(self):
        for item in self.inventory:
            print(item.name)