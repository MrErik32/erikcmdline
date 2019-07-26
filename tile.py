class Tile:
    def __init__(self, x, y, occupied=False, occupant=None):
        self.x = x
        self.y = y
        self.occupied = occupied
        self.occupant = occupant
    
    def occupy(self, object):
        self.occupant = object
        self.occupied = True
    
    def vacate(self):
        self.occupant = None
        self.occupied = False