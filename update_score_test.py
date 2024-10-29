import unittest

from .update_score import average_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        scores_dict = {"Test 1": 31, "Test 2": 34, "Test 3": 54}
        expected = 39.66666666
        actual = average_scores(scores_dict)
        self.assertAlmostEqual(expected, actual)

    def test_average_five(self):
        scores = {"Test 1": 10, "Test 2": 20, "Test 3": 30, "Test 4": 40, "Test 5": 50}
        expected = 30
        actual = average_scores(scores)
        self.assertAlmostEqual(expected, actual)

    def test_average_empty(self):
        scores = {}
        with self.assertRaises(ValueError):
            average_scores(scores)