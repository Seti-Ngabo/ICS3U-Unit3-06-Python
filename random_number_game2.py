#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program guesses a random number

import random


def main():
    # this function checks if the random number is correct
    guessed_number = random.randint(0, 50)
    # a number between 0 and 50

    # input
    guessed_string = input("Enter the number between 0 and 50 (integer): ")
    print("")

    # process and output
    try:
        user_guessed_number = int(guessed_string)
        if user_guessed_number == guessed_number:
            print("Correct")
            print("")
        else:
            print("wrong, try again")
            print("")
    except Exception:
        print("That number is not a valid integer, try again.")
        print("")
    finally:
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
