"""
Program: tuples.py
Author: Cameron Dehning
"""


def sort_list(data: list[int]):
    data.sort()
    # the sort method modifies the list in place, so we don't need to return anything


def search_list(data: list[int], num: int) -> bool:
    # return True if the number is in the list, otherwise return False
    return num in data


if __name__ == "__main__":
    data = [4, 3, 2, 4]
    sort_list(data)
    print(data)
    print(search_list(data, 3))
