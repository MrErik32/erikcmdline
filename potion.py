
class Potion:
    def __init__(self, size="Small", stack_size=1):
        self.name = f"{size} Potion"
        if size == "Small":
            self.healing = 10
        elif size == "Medium":
            self.healing = 25
        else:
            self.healing == 50
        self.stack_size = stack_size

    def use(self, user):
        pass