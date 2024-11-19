#!/usr/bin/env python3
import sys

def main():
    # Check the number of parameters passed
    if len(sys.argv) != 2:
        print("none")
        return

    # Get the parameter from the command line
    parameter = sys.argv[1]

    # Prompt the user to enter a word
    user_input = input("What was the parameter? ")

    # Compare the user's input with the parameter
    if user_input == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()