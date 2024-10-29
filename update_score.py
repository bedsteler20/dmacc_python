import unittest


def input_int(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a valid integer.")
        return input_int(prompt)


def get_test_scores():
    scores_dict = dict()
    num_inputs = input_int("Enter the number of students: ")

    for _ in range(num_inputs):
        name = input("Enter student name: ")
        score = input("Enter student score: ")
        scores_dict[name] = int(score)

    return scores_dict


def average_scores(scores: dict[any, int]) -> float:
    if len(scores) == 0:
        raise ValueError("The dictionary is empty.")
    total = 0
    for score in scores.values():
        total += score
    return total / len(scores)


def main():
    scores = get_test_scores()
    avg = average_scores(scores)
    print(f"The average score is {avg}.")


if __name__ == "__main__":
    main()


class MyTestCase(unittest.TestCase):

    def test_average(self):
        # Arrange
        scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666  # 7 decimal places, remove one and see the test fail
        # Act
        actual = average_scores(scores_dict)
        # Assert
        self.assertAlmostEqual(expected, actual)
