import random
import json

player_data = {
    "name": "",
    "hp": 100,
    "mp": 100,
    "sp": 100,
    "str": 10,
    "dex": 10,
    "pow": 10,
    "wil": 10,
    "vit": 10,
    "agi": 10,
    "chr": 10,
    "end": 10,
    "luk": 10,
}


def create_character():
    name = input("Please enter your name: ")
    player_data["name"] = name
    print("Please select a race for your player:")
    print("1. Human")
    print("--- +5 Dexterity")
    print("--- +5 Charisma")
    print("--- +5 Luck")
    print("2. Orc")
    print("--- +5 Strength")
    print("--- +5 Willpower")
    print("--- +5 Endurance")
    print("3. Frostmere")
    print("--- +10 Strength")
    print("--- +5 Vitality")


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
