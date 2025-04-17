import unittest
from datetime import datetime
from utils.time_utils import get_formatted_timestamp

class TestTimestamp(unittest.TestCase):
    def test_timestamp_formatting(self):
        test_cases = [
            (datetime(2023, 12, 31, 23, 59), "2023-12-31 23:59"),
            (datetime(2023, 1, 2, 3, 4), "2023-01-02 03:04"),
            (datetime(2023, 1, 1, 0, 0), "2023-01-01 00:00")
        ]
        for time_input, expected in test_cases:
            with self.subTest(time_input=time_input):
                self.assertEqual(get_formatted_timestamp(time_input), expected)

if __name__ == '__main__':
    unittest.main()