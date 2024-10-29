"""
Author: Cameron Dehning
Description: This program will ask the user how many items they want to add to a list, then ask the user to input that many numbers between 1 and 100. The program will then print out the list of numbers.
"""

data = []
stop_at = int(input("How many items do you want to add to the list?: "))

while len(data) < stop_at:
    value = int(input("Enter a number to add to the list: "))
    while value < 1 or value > 100:
        user_input = input("Invalid input. Please enter a number between 1 and 100: ")
        if user_input == "exit":
            break
        value = int(user_input)
    data.append(value)

for num in data:
    print(num)
