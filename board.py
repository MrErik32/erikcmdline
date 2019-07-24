class Board:
  
    def __init__(self, height=3, width=3):
        self.height = height
        self.width = width
        self.board = [ [0]*width for _ in range(height) ]

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    print('[   ]', end='')
                elif self.board[i][j].name == 'Hero':
                    print('[ H ]', end='')
                elif 'Potion' in self.board[i][j].name:
                    print('[ p ]', end='')
                if j == self.width - 1:
                    print('')

    def clear_field(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = 0
    
    def check_location(self, x, y):
        return self.board[x][y]

    def add(self, object, x, y):
        if self.check_location(x,y) == 0:
            self.board[x][y] = object
        else:
            print(f"Tile {x},{y} already occupied")
    
    def delete(self, x, y):
        if self.check_location(x,y) != 0:
            self.board[x][y] = 0
        else:
            print(f"Tile {x},{y} already empty")

    def find_adjacent(self, x, y):
        adjacent_list = []

        if x - 1 >= 0 and self.check_location(x-1, y) == 0:
            adjacent_list.append([x-1,y])
        if x + 1 <= self.width -1 and self.check_location(x+1, y) == 0:
            adjacent_list.append([x+1,y])
        if y - 1 >= 0 and self.check_location(x, y-1) == 0:
            adjacent_list.append([x,y-1])
        if y + 1 <= self.width -1 and self.check_location(x, y+1) == 0:
            adjacent_list.append([x,y+1]) 
        
        return adjacent_list

    def spawned(self):
        spawned = []
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] != 0:
                    spawned.append(self.board[i][j])
        return spawned