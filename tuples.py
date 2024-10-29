"""
Program: tuples.py
Author: Cameron Dehning
"""

import json
from typing import Tuple


def write_to_file(data: Tuple[str, list[int]]):
    name, scores = data

    with open("student_info.txt", "a") as file:
        file.write(f"{name} = {scores}\n")


def get_student_info(name: str) -> Tuple:
    data = (name,[])
    while True:
        try:
            inp = input(f"Enter a score: ")
            if inp == "q":
                break
            else:
                data[1].append(int(inp))
        except ValueError:
            print("Please enter a valid number.")
    write_to_file(data)


def read_from_file():
    data = {}
    with open("student_info.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            name, json_scores = line.split(" = ")
            scores = json.loads(json_scores)
            data[name] = scores
    return data


if __name__ == "__main__":
    open("student_info.txt", "w").close()
    get_student_info("Cameron")
    print(read_from_file())