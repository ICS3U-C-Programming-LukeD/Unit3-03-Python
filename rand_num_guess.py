#!/usr/bin/env python3

# Created By: Luke
# Date: March 21, 2025
# Asks user to guess a random number using a random number generator

# Adds random module
import random

# Adds math module
import math


def main():
    # Generates a random number from 0 to 9
    random_number = random.randint(0, 9)
    # Prompts user to guess a number
    user_guess = int(input(("Guess a number from 0 to 9: ")))
    # prints corresponding answers depending on if the user was right or not
    if user_guess == random_number:
        print("You got it right")
    else:
        print("You got it wrong! the correct number was ", random_number)


if __name__ == "__main__":
    main()
