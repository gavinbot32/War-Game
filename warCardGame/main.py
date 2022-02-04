#Gavin Murdock
#War Card Game
#2/2/22
import random
from warClasses import *
from commonGameFunctions import *
def main():
    print("\t\tWelcome to War\n")
    names =[]
    for i in range(2):
        name = input("enter players name")
        names.append(name)
    game = War_Game(names)
    again = None
    while again != "n":
        again = askYorN("\nDo you want to play again?: ")
main()