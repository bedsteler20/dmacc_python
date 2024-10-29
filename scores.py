"""
Program: scores.py
Author: Cameron Dehning
"""


def average_scores(*args, **kwargs):
    output = "Result: "
    for key, value in kwargs.items():
        output += f"{key}: {value} "
    output += f"gpa: {sum(args) / len(args):.2f}"
    return output


if __name__ == "__main__":
    print(
        average_scores(
            4,
            3,
            2,
            4,
            first_name="Cameron",
            last_name="Dehning",
            major="Computer Science",
        )
    )
    print(
        average_scores(
            3,
            2,
            3,
            9,
            8,
            23,
            first_name="John",
            last_name="Doe",
            major="Math",
        )
    )

    print(
        average_scores(
            3,
            2,
            21,
            9,
            8,
            first_name="John",
            last_name="Doe",
            major="Math",
        )
    )
