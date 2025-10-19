# --------------------------------------------
# Project: Dice Roller Simulator
# File : 01_basic_dice_roll.py
# Week: 3 – File Handling & Functions
# Author: Faiz Ur Rehman Ashrafi
# Goal: Simulate rolling a dice (1–6) using random numbers.
# Concepts Used: Random module, functions
# --------------------------------------------

from random import randint
from time import sleep


# Function: Dice Simulator
def dice_simulator() -> int:
    """Return a random number between 1 and 6."""
    return randint(1, 6)


print("=== Welcome to Dice Simulator ===")
print("DICE ROLL (1–6)")


def main() -> None:
    """Main function to run the dice simulation."""
    while True:
        user: str = input("\nSimulate Dice? (yes/y to roll, any key to exit): ")

        if user.lower() in ("y", "yes"):
            print("Rolling the dice...")
            sleep(1)
            print("...", end="")
            sleep(1)

            result: int = dice_simulator()
            print(f"\nYour Dice Number: {result}")
        else:
            print("Thanks for playing. See you again!")
            break


if __name__ == "__main__":
    main()
