
import unittest

from subtractTwoNumbers import subtractNumbers

class TestDivideNumbers(unittest.TestCase):
    """Test subtract two numbers functionality"""
    def test_is_an_integer(self):
        type(self) == int
    def test_subtraction(self):
        self.assertEqual(subtractNumbers(6, 2), 4)
        self.assertEqual(subtractNumbers(-3, 1), -4)
        self.assertEqual(subtractNumbers(7, -2), 9)
if __name__ == '__main__':
    unittest.main()