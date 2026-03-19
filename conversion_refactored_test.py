import unittest

from conversion_refactored import convert, ConversionNotPossible

class TestConversions(unittest.TestCase):

    # --- Temperature Data  ---
    test_cases_temp = [
        (0.0, "celsius", "kelvin", 273.15),
        (-273.15, "celsius", "kelvin", 0.0),
        (32.0, "fahrenheit", "celsius", 0.0),
        (212.0, "fahrenheit", "celsius", 100.0),
        (0.0, "fahrenheit", "kelvin", 255.37222),
        (273.15, "kelvin", "fahrenheit", 32.0),
        (3000, "kelvin", "celsius", 2726.85),
    ]

    # --- Distance Data ---
    test_cases_dist = [
        (1, "mile", "meters", 1609.344),
        (1760, "yards", "miles", 1.0),
        (100, "meter", "yard", 109.361),
    ]

    def test_all_temperatures(self):
        """Replaces all 6 old test functions with one loop"""
        for val, from_u, to_u, expected in self.test_cases_temp:
            with self.subTest(f"{from_u} to {to_u}"):
                # Using places=2 because some temp formulas have long decimals
                self.assertAlmostEqual(convert(val, from_u, to_u), expected, places=2)

    def test_all_distances(self):
        """Tests distances"""
        for val, from_u, to_u, expected in self.test_cases_dist:
            with self.subTest(f"{from_u} to {to_u}"):
                self.assertAlmostEqual(convert(val, from_u, to_u), expected, places=2)

    def test_case_and_spaces(self):
        """Ensures ' MILES ' and 'miles' and 'Miles' all work"""
        self.assertAlmostEqual(convert(1, "  MILES  ", "meter"), 1609.344, places=2)

    def test_incompatible_units(self):
        """Ensures you can't convert miles to celsius"""
        with self.assertRaises(ConversionNotPossible):
            convert(10, "miles", "celsius")

if __name__ == '__main__':
    unittest.main()