"""
Author: Cameron Dehning
Purpose: Calculate the average of two scores.
"""
import sys
PROMPT_NUM = 2

def main():
    # Get the user's first and last name
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    scores = []

    # Get the scores from the user
    for i in range(PROMPT_NUM):
        try:
            score = float(input(f"Enter score {str(i+1):}: "))
            if score < 0:
                raise ValueError("Score must be greater than or equal to 0.")
            scores.append(score)
        except ValueError:
            print("Please enter a valid number.")
            sys.exit(1) # Exit the program with an error code

    # Calculate the average score
    average = sum(scores) / len(scores)
    print(f"{last_name}, {first_name} average score: {average:.2f}")


# Call the main function if the script is executed
if __name__ == '__main__':
    main()