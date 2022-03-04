"""
"""

import unittest
from unittest import TestCase

import example_b


class TestExampleB(TestCase):
    """
    """
    def test_add(self):
        """
        """
        self.assertEqual(example_b.add(2, 3), 5)
        self.assertEqual(example_b.add(-3, 3), 0)

    def test_sub(self):
        """
        """
        self.assertEqual(example_b.sub(5, 2), 3)
        self.assertEqual(example_b.sub(-2, -3), 1)

    def test_mult(self):
        """
        """
        self.assertEqual(example_b.mult(2, 3), 6)
        self.assertEqual(example_b.mult(1, 10), 10)

    def test_div(self):
        """
        """
        self.assertEqual(example_b.div(10, 2), 5)
        self.assertEqual(example_b.div(6, 3), 2)


if __name__ == "__main__":
    unittest.main()
