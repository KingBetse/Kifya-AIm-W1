import unittest
import pandas as pd
from main import calculate_mean

class TestMain(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]
        })

    def test_calculate_mean_column_a(self):
        result = calculate_mean(self.data, 'A')
        self.assertEqual(result, 3.0)

    def test_calculate_mean_column_b(self):
        result = calculate_mean(self.data, 'B')
        self.assertEqual(result, 30.0)

if __name__ == "__main__":
    unittest.main()