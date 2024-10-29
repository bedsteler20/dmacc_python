"""
Author: Cameron Dehning
Description: This code prompts the user to enter a subscription level and then displays the corresponding price based on the input.

Example:
What level do you want to subscribe at: gold
Price: $50

What level do you want to subscribe at: silver
Price: $40

What level do you want to subscribe at: platinum
Price: $60

What level do you want to subscribe at: bronze
Price: $30

What level do you want to subscribe at: free
Price: $0
"""

level = input("What level do you want to subscribe at:")

if level == "platinum":
    print("Price: $60")
elif level == "gold":
    print("Price: $50")
elif level == "silver":
    print("Price: $40")
elif level == "bronze":
    print("Price: $30")
elif level == "free":
    print("Price: $0")
else:
    print("Invalid level")
