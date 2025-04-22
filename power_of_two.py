# Author: 2025 Mikhail Ibrahim
# Date: Apr 21, 2025
# Description: A crash-proof Python program that calculates and displays
# the square (power of 2) of all numbers from 0 up to a user-entered whole number.
# It uses a for loop and handles all invalid entries.

print(
    "Welcome! This program prints the squares of numbers from 0 up to the number you enter."
)

user_input = input("Enter a non-negative whole number: ")

# Try to convert the user input to an integer and validate
try:
    number = int(user_input)

    if number < 0:
        print("Error: Please enter a non-negative number.")

    else:
        # Valid input - proceed to print squares using a for loop
        for i in range(number + 1):
            print(f"{i}^2 = {i**2}")

except ValueError:
    print("Error: Please enter digits only (no letters, symbols, or decimals).")
# Author: 2025 Mikhail Ibrahim
# Date: Apr 21, 2025
# Description: A crash-proof Python program that calculates and displays
# the square (power of 2) of all numbers from 0 up to a user-entered whole number.
# It uses a for loop and handles all invalid entries.

print(
    "Welcome! This program prints the squares of numbers from 0 up to the number you enter."
)

user_input = input("Enter a non-negative whole number: ")

# Try to convert the user input to an integer and validate
try:
    number = int(user_input)

    if number < 0:
        print("Error: Please enter a non-negative number.")

    else:
        # Valid input - proceed to print squares using a for loop
        for i in range(number + 1):
            print(f"{i}^2 = {i**2}")

except ValueError:
    print("Error: Please enter digits only (no letters, symbols, or decimals).")
