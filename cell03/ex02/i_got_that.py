#!/usr/bin/env python3

def main():
    while True:
        user_input = input("What you gotta say? : ")

        # Check if the input is "STOP"
        if user_input.strip().upper() == "STOP":
            break
        
        print("I got that! Anything else? : ")

if __name__ == "__main__":
    main()