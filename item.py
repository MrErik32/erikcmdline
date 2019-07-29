from point import Point

class Item:
    location = None

    def __init__(self, name="New Item"):
        self.name = name

    def set_location(self, x, y):
            self.location = Point(x, y)