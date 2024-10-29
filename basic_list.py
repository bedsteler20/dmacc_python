"""
Program: basic_list.py
Author: Cameron Dehning
"""


def get_input() -> str:
    return input("Enter a number: ")


def make_list(num: int):
    data = []
    for _ in range(num):
        inp = get_input()
        if inp.isnumeric():
            data.append(int(inp))
        else:
            raise ValueError("Please enter a valid number.")
    return data


if __name__ == "__main__":
    try:
        print(make_list(1))
        print(make_list(2))
        print(make_list(3))

    except ValueError as e:
        print(e)
