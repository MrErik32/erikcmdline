from tile import Tile
from point import Point
from player import Player

class Board:

    board = []
  
    def __init__(self, height=3, width=3):
        self.height = height
        self.width = width
        self.board = [ [0]*width for _ in range(height) ]
        self.clear_field()

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                if not self.board[i][j].occupied:
                    print('[   ]', end='')
                elif type(self.board[i][j].occupant) == Player:
                    print('[ H ]', end='')
                elif 'Potion' in self.board[i][j].occupant.name:
                    print('[ p ]', end='')
                if j == self.width - 1:
                    print('')

    def clear_field(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = Tile(Point(i,j))
    
    def within_bounds(self, x, y):
        if x <= self.height and x >= 0 and y <= self.width and y >= 0:
            return True
        else:
            return False

    def point_within_bounds(self, point):
        if point.x <= self.height and point.x >= 0 and point.y <= self.width and point.y >= 0:
            return True
        else:
            return False

    def get_tile(self, x, y):
        if self.within_bounds(x, y):
            return self.board[x][y]

    def tile_occupied(self, x, y):
        if self.within_bounds(x, y):
            return self.board[x][y].occupied
        else:
            print("Location out of bounds")

    def add(self, object, x, y):
        if not self.tile_occupied(x,y):
            self.board[x][y].occupy(object)
            object.set_location(x, y)
        else:
            print(f"Tile {x},{y} already occupied")
    
    def delete(self, x, y):
        if self.tile_occupied(x,y):
            self.board[x][y].vacate()
        else:
            print(f"Tile {x},{y} already empty")

    def find_adjacent(self, x, y):
        if self.within_bounds(x, y):
            adjacent_list = []

            if x - 1 >= 0 and not self.tile_occupied(x-1, y):
                adjacent_list.append(self.board[x-1][y])
            if x + 1 <= self.width -1 and not self.tile_occupied(x+1, y):
                adjacent_list.append(self.board[x+1][y])
            if y - 1 >= 0 and not self.tile_occupied(x, y-1):
                adjacent_list.append(self.board[x][y-1])
            if y + 1 <= self.width -1 and not self.tile_occupied(x, y+1):
                adjacent_list.append(self.board[x][y+1]) 
            
            return adjacent_list
        else:
            print("Location out of bounds")

    def spawned(self):
        spawned = []
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].occupied:
                    spawned.append(self.board[i][j])
        return spawned
    
    def move(self, start_location, end_location):
        if self.point_within_bounds(start_location) and self.point_within_bounds(end_location):
            adjacent_tiles = self.find_adjacent(start_location.x, start_location.y)
            start_tile = self.board[start_location.x][start_location.y]
            end_tile = self.board[end_location.x][end_location.y]
            if end_tile in adjacent_tiles and not end_tile.occupied:
                mover = start_tile.occupant
                start_tile.vacate()
                end_tile.occupy(mover)
                mover.set_location(end_location.x, end_location.y)
            else:
                print("Can't move there")
        else:
            print("Not a valid location to move to")