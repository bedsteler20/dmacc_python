"""
Program: cast_to_int.py
Author:  Cameron Dehning
Date: 08/29/2024

This program takes a string and casts it to an integer
and outputs the integer.
"""


def main():
    # Get a string from the user
    user_input = input("Enter a number: ")

    # Cast the string to a float and then to an integer
    # if casted directly to an int it will throw a ValueError
    float_number = float(user_input)
    number = int(float_number)

    # Output the integer
    print(f"The integer is: {number}")


# Only run the main function if this script is executed directly
# and not imported as a module
if __name__ == "__main__":
    main()

# Input    Expected Output     Actual Output
# 7        7                   7
# 6.872    6                   6
# UwU      ValueError          ValueError
