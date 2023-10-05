import unittest
from mypackage.module0 import calculate_rms

class TestCalculateRMS(unittest.TestCase):

    def test_rms_with_empty_list(self):
        # Test RMS calculation with an empty list.
        numbers = []
        self.assertEqual(calculate_rms(numbers), 0.0)

    def test_rms_with_positive_numbers(self):
        # Test RMS calculation with positive numbers.
        numbers = [2, 4, 6, 8, 10]
        self.assertAlmostEqual(calculate_rms(numbers), 6.6332495807108, places=6)

    def test_rms_with_negative_numbers(self):
        # Test RMS calculation with negative numbers.
        numbers = [-1, -3, -5, -7, -9]
        self.assertAlmostEqual(calculate_rms(numbers), 5.744562646538029, places=6)

if __name__ == "__main__":
    unittest.main()
