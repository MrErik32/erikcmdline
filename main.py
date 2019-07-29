import sys
from player import Player
from unit import Unit
from board import Board
from potion import Potion
from point import Point

hero = Player("Hero")
board = Board()

def main():
    board.add(hero, 1, 1)
    loop()

def loop():
    while True:
        command = input("> ")

        # Command verification
        if command[0:3].lower() == "say":
            say(command[4:])
        
        elif command[0:3].lower() == "map":
            board.print()

        elif command[0:4].lower() == "loot":
            loot(command[5:])

        elif command[0:4].lower() == "move":
            move(command[5:])
        
        elif command[0:5].lower() == "spawn":
            spawn(command[6:])

        elif command[0:9].lower() == "inventory":
            hero.list_inventory()

        elif command[0:4].lower() == "exit":
            sys.exit()
        else:
            print("No recognizable command entered")

def move(command):
    if command != '':
        if command.lower() == "north":
            board.move(hero.location, Point(hero.location.x-1, hero.location.y))
        elif command.lower() == "south":
            board.move(hero.location, Point(hero.location.x+1, hero.location.y))
        elif command.lower() == "east":
            board.move(hero.location, Point(hero.location.x, hero.location.y+1))
        elif command.lower() == "west":
            board.move(hero.location, Point(hero.location.x, hero.location.y-1))
        else:
            print("Not a recognized direction")
    else:
        print("Need a direction to move in")

def loot(command):
    if command == '':
        loc = command.split(',')
        loc = list(map(int, loc))
        hero.check_for_loot(board.get_tile(loc[0], loc[1]))
    else:
        print("Need a point to loot")

def say(words):
    print(f"{hero.name} says: '{words}'")

def spawn(command):
    if "potion" in command.lower():
        if "at" in command:
            pointer1 = command.find('at')
            pointer2 = command.find(',')
            x = int(command[(pointer1 + 3):pointer2])
            y = int(command[pointer2+1:])
            board.add(Potion(), x, y)
        else:
            print("No location specified")
    else:
        print("Not a spawnable item")

if __name__ == "__main__":
    main()