#!/usr/bin/env python3

def main():
    # Loop through numbers 0 to 10 to create multiplication tables
    for i in range(11):
        # Create the multiplication table for the current number
        table = [i * j for j in range(11)]
        # Format the output as required
        print(f"Table de {i}: {' '.join(map(str, table))}")

if __name__ == "__main__":
    main()