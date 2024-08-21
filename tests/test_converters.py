import unittest
from converters import celsius_to_fahrenheit

class TestConverters(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        c = 0
        expected = 32
        result = celsius_to_fahrenheit(c)
        self.assertEqual(result, expected)
