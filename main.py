import random
import json
from misc_funct import *

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


def change_stats(keys, nums):
    z = 0
    for i in keys:
        player_data[i] += nums[z]
        z += 1


def show_stats():
    print("Name:", player_data["name"])
    print(
        "Strength:",
        player_data["str"],
        "| Dexterity:",
        player_data["dex"],
        "| Power:",
        player_data["pow"],
    )
    print(
        "Willpower:",
        player_data["wil"],
        "| Vitality:",
        player_data["vit"],
        "| Agility:",
        player_data["agi"],
    )
    print(
        "Charisma:",
        player_data["chr"],
        "| Endurance:",
        player_data["end"],
        "| Luck:",
        player_data["luk"],
    )


def race_list():
    print()
    print_border()
    print("1. Human     | 4. High Elf  | 7. Aetherian  | 10. Bragasilian")
    print(">+5 Dexterity| >+10 Power   | >+10 Dexterity| >+5 Power")
    print(">+5 Charisma | >+5 Willpower| >+5 Power     | >+5 Willpower")
    print(">+5 Luck     | 5. Sea Elf   | 8. Dethrian   | >+5 Agility")
    print("2. Orc       | >+5 Dexterity| >+5 Strength  |")
    print(">+5 Strength | >+5 Agility  | >+5 Power     |")
    print(">+5 Willpower| >+5 Charisma | >+5 Vitality  |")
    print(">+5 Endurance| 6. Goblin    | 9. Dwarf      |")
    print("3. Frostmere | >+5 Dexterity| >+5 Strength  |")
    print(">+10 Strength| >+5 Agility  | >+5 Dexterity |")
    print(">+5 Vitality | >+5 Luck     | >+5 Vitality  |")
    print_border()
    print()


def class_list():
    print()
    print_border()
    print("1. Warrior    | 4. Palladin")
    print(">+10 Strength | >+10 Strength")
    print(">+5 Dexterity | >+10 Power")
    print(">+10 Vitality | >+10 Willpower")
    print(">+5 Endurance | 5. Shadow Mage")
    print("2. Mage       | >+10 Power")
    print(">+15 Power    | >+10 Dexterity")
    print(">+10 Willpower| >+5 Agility")
    print(">+5 Agility   | >+5 Luck")
    print("3. Thief      | 6. Rogue Knight")
    print(">+10 Dexterity| >+10 Strength")
    print(">+10 Agility  | >+10 Dexterity")
    print(">+5 Charisma  | >+5 Charisma")
    print(">+5 Luck      | >+5 Luck")
    print_border()
    print()


def create_character():
    name = input("Please enter your name: ")
    player_data["name"] = name
    race_list()
    while True:
        race = input("Please select a race for your player:")
        three_list = [5, 5, 5]
        two_list = [10, 5]
        if repr_int(race):
            race = int(race)
            if race == 1:
                change_stats(["dex", "chr", "luk"], three_list)
                break
            elif race == 2:
                change_stats(["str", "wil", "end"], three_list)
                break
            elif race == 3:
                change_stats(["str", "vit"], two_list)
                break
            elif race == 4:
                change_stats(["pow", "wil"], two_list)
                break
            elif race == 5:
                change_stats(["dex", "agi", "chr"], three_list)
                break
            elif race == 6:
                change_stats(["dex", "agi", "luk"], three_list)
                break
            elif race == 7:
                change_stats(["dex", "pow"], two_list)
                break
            elif race == 8:
                change_stats(["str", "pow", "vit"], three_list)
                break
            elif race == 9:
                change_stats(["str", "dex", "vit"], three_list)
                break
            elif race == 10:
                change_stats(["pow", "wil", "agi"], three_list)
                break
            else:
                print("Please enter a valid choice")
    show_stats()


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


main_menu()
