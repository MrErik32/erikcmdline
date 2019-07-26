from tile import Tile

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
                elif self.board[i][j].occupant.name == 'Hero':
                    print('[ H ]', end='')
                elif 'Potion' in self.board[i][j].occupant.name:
                    print('[ p ]', end='')
                if j == self.width - 1:
                    print('')

    def clear_field(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = Tile(i, j)
    
    def tile_occupied(self, x, y):
        if x <= self.height and y <= self.width:
            return self.board[x][y].occupied
        else:
            print("Location out of bounds")

    def add(self, object, x, y):
        if not self.tile_occupied(x,y):
            self.board[x][y].occupy(object)
        else:
            print(f"Tile {x},{y} already occupied")
    
    def delete(self, x, y):
        if self.tile_occupied(x,y):
            self.board[x][y].vacate()
        else:
            print(f"Tile {x},{y} already empty")

    def find_adjacent(self, x, y):
        if x <= self.height and y <= self.width:
            adjacent_list = []

            if x - 1 >= 0 and not self.tile_occupied(x-1, y):
                adjacent_list.append([x-1,y])
            if x + 1 <= self.width -1 and not self.tile_occupied(x+1, y):
                adjacent_list.append([x+1,y])
            if y - 1 >= 0 and not self.tile_occupied(x, y-1):
                adjacent_list.append([x,y-1])
            if y + 1 <= self.width -1 and not self.tile_occupied(x, y+1):
                adjacent_list.append([x,y+1]) 
            
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