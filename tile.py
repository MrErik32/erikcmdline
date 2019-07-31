class Tile(object):
    def __init__(self, point, occupied=False, occupant=None):
        self.position = point
        self.occupied = occupied
        self.occupant = occupant
    
    def occupy(self, object):
        self.on_enter()
        self.occupant = object
        self.occupied = True
    
    def vacate(self):
        self.on_exit() 
        self.occupant = None
        self.occupied = False

    def on_enter(self):
        pass
    
    def on_exit(self):
        pass