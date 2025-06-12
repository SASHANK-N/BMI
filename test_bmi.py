import unittest
from bmi import calculate_bmi

class TestBMICalculator(unittest.TestCase):
    def test_valid_bmi(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.86, places=2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(70, 0)
