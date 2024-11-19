#!/usr/bin/env python3

def main():
    # Prompt the user for a string
    user_input = input("Please enter a string: ")

    # Swap the case of the letters in the string
    swapped_case = user_input.swapcase()

    # Display the resulting string
    print(swapped_case)

if __name__ == "__main__":
    main()