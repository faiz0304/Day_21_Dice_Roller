# --------------------------------------------
# Project: Dice Roller Simulator
# File : 02_dice_roll_store_data.py
# Week: 3 – File Handling & Functions
# Author: Faiz Ur Rehman Ashrafi
# Goal: Simulate rolling a dice (1–6) and store results in a file.
# Concepts Used: Random module, functions, file handling
# --------------------------------------------

from random import randint
from time import sleep


def dice_simulator() -> int:
    """Return a random number between 1 and 6."""
    return randint(1, 6)


def store_data(filename: str, result: int) -> None:
    """Save dice roll result into the given file."""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"Dice Simulate: {result}\n")
    except FileNotFoundError:
        print(f"ERROR: {filename} not found.")
    except Exception as e:
        print("ERROR: An unexpected error occurred:", e)


print("=== Welcome to Dice Simulator ===")
print("DICE ROLL (1–6)")


def main() -> None:
    """Main function to roll dice and save results."""
    filename: str = input("Enter file name to store dice results: ")

    while True:
        user: str = input("\nSimulate Dice? (yes/y to roll, any key to exit): ")

        if user.lower() in ("y", "yes"):
            print("Rolling the dice...")
            sleep(1)
            print("...", end="")
            sleep(1)

            result: int = dice_simulator()
            print(f"\nYour Dice Number: {result}")

            store_data(filename, result)
        else:
            print("Thanks for playing. See you again!")
            break


if __name__ == "__main__":
    main()
