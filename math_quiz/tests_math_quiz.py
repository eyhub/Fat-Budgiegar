import unittest
from math_quiz import random_number_generator, random_operator_generator, expression_generator

class TestMathGame(unittest.TestCase):

    def test_random_number_generator(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_generator(self):
        """Test if the random operator generated is one of the specified operators."""
        operators = {'+', '-', '*'}
        for _ in range(1000):  # Test multiple times to confirm all operators appear
            op = random_operator_generator()
            self.assertIn(op, operators)

    def test_expression_generator(self):
        """Test if expression_generator correctly computes problems and results."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 3, '*', '4 * 3', 12),
            # Additional cases
            (0, 0, '+', '0 + 0', 0),
            (1, 1, '-', '1 - 1', 0),
            (6, 5, '*', '6 * 5', 30),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = expression_generator(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
