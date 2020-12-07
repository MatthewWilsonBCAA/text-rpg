import random
import json

player_data = {"name": "", "hp": 100, "mp": 100, "sp": 100}


def create_character():
    name = input("Please enter your name: ")


def load_character():
    print("Loading...")


def main_menu():
    while True:
        print("Welcome to my text-based rpg")
        print("1 - New Game")
        print("2 - Load Game")
        print("3 - Exit")
        print("Type the corrisponding number for that option")
        choice = int(input())
        if choice == 1:
            create_character()
            break
        elif choice == 2:
            load_character()
            break
        elif choice == 3:
            exit()
        else:
            continue
