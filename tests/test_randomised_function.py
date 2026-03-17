import unittest
from unittest.mock import patch
from lecture import randomised_function


class MyTestCase(unittest.TestCase):

    @patch("random.randint", return_value=3)
    def test_randomised_function_returns_software(self, mock_randint):
        self.assertEqual('software', randomised_function())

    @patch("random.randint", return_value=8)
    def test_randomised_function_returns_engineering(self, mock_randint):
        self.assertEqual('engineering', randomised_function())


if __name__ == '__main__':
    unittest.main()