import sys
from unit import Unit
from board import Board
from potion import Potion

hero = Unit("Hero")
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
            pass
        
        elif command[0:5].lower() == "spawn":
            spawn(command[6:])

        elif command[0:4].lower() == "exit":
            sys.exit()
        else:
            print("No recognizable command entered")

def say(words):
    print(f"{hero.name} says: '{words}'")

def spawn(command):
    if "Potion" in command or "potion" in command:
        if "at" in command:
            pointer1 = command.find('at')
            pointer2 = command.find(',')
            x = int(command[(pointer1 + 3):pointer2])
            y = int(command[pointer2+1:])
            board.add(Potion(), x, y)
        else:
            print("No location specified")
    else:
        print("Not a valid command")

if __name__ == "__main__":
    main()