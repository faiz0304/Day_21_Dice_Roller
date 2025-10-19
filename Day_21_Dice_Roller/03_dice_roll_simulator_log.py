# --------------------------------------------
# Project: Dice Roller Simulator
# File : 03_dice_roll_simulator_log.py
# Week: 3 – File Handling & Functions
# Author: Faiz Ur Rehman Ashrafi
# Goal: Simulate rolling a dice (1–6) and store results with real-time logs.
# Concepts Used: Random module, functions, file handling, datetime
# --------------------------------------------

from random import randint
from time import sleep
from datetime import datetime


def dice_simulator() -> int:
    """Return a random number between 1 and 6."""
    return randint(1, 6)


def store_data(filename: str, result: int) -> None:
    """Log dice roll results with timestamp into a file."""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            timestamp: str = datetime.now().strftime("%d-%m-%Y | %H:%M:%S")
            file.write(f"Dice Roll: {result} | {timestamp}\n")
    except Exception as e:
        print("ERROR: Unable to write to file:", e)


print("=== Welcome to Dice Simulator ===")
print("DICE ROLL (1–6)")


def main() -> None:
    """Main function to simulate and log dice rolls."""
    filename: str = "dice_simulate_history.txt"

    while True:
        user: str = input("\nPress ENTER to roll or type 'q' to quit: ")

        if user.lower() == "q":
            print("Thanks for playing. See you again!")
            break

        print("Rolling the dice...")
        sleep(1)
        print("...", end="")
        sleep(1)

        result: int = dice_simulator()
        print(f"\nYour Dice Number: {result}")

        store_data(filename, result)


if __name__ == "__main__":
    main()
