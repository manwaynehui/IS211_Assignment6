# test.py
import unittest
from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit,
)

class TestTemperatureConversions(unittest.TestCase):

    test_cases_celsius_to_kelvin = [
        (0.0, 273.15),
        (-273.15, 0.0),
        (200.0, 473.15),
        (-10.0, 263.15),
        (-100, 173.15),
    ]

    test_cases_celsius_to_fahrenheit = [
        (0.0, 32.0),
        (-40.0, -40.0),
        (100.0, 212.0),
        (200.0, 392.0),
        (-58, -72.4),
    ]

    test_cases_fahrenheit_to_celsius = [
        (32.0, 0.0),
        (-46.0, -43.33333),
        (212.0, 100.0),
        (392.0, 200.0),
        (-58, -50.0),
    ]

    test_cases_fahrenheit_to_kelvin = [
        (0.0,   255.37222),
        (-40.0, 233.15),
        (32.0,  273.15),
        (212.0, 373.15),
        (459.67, 510.74444),
    ]

    test_cases_kelvin_to_fahrenheit = [
        (0.0, -459.67),
        (273.15, 32.0),
        (373.15, 212.0),
        (283.15, 50),
        (75, -324.67),
    ]

    test_cases_kelvin_to_celsius = [
        (0.0, -273.15),
        (273.15, 0.0),
        (373.15, 100.0),
        (3000,2726.85),
        (-3000,-3273.15)
    ]

    def test_convert_celsius_to_kelvin(self):
        for celsius, expected in self.test_cases_celsius_to_kelvin:
            self.assertAlmostEqual(
                convertCelsiusToKelvin(celsius),
                expected,
                places=5,
                msg=f"Celsius {celsius} → Kelvin {expected}"
            )

    def test_convert_celsius_to_fahrenheit(self):
        for celsius, expected in self.test_cases_celsius_to_fahrenheit:
            self.assertAlmostEqual(
                convertCelsiusToFahrenheit(celsius),
                expected,
                places=5,
                msg=f"Celsius {celsius} → Fahrenheit {expected}"
            )

    def test_convert_fahrenheit_to_celsius(self):
        for fahrenheit, expected in self.test_cases_fahrenheit_to_celsius:
            self.assertAlmostEqual(
                convertFahrenheitToCelsius(fahrenheit),
                expected,
                places=5,
                msg=f"Fahrenheit {fahrenheit} → Celsius {expected}"
            )

    def test_convert_fahrenheit_to_kelvin(self):
        """Fahrenheit → Kelvin"""
        for fahrenheit, expected in self.test_cases_fahrenheit_to_kelvin:
            self.assertAlmostEqual(
                convertFahrenheitToKelvin(fahrenheit),
                expected,
                places=5,
                msg=f"Fahrenheit {fahrenheit} → Kelvin {expected}"
            )

    def test_convert_kelvin_to_fahrenheit(self):
        for kelvin, expected in self.test_cases_kelvin_to_fahrenheit:
            self.assertAlmostEqual(
                convertKelvinToFahrenheit(kelvin),
                expected,
                places=5,
                msg=f"Kelvin {kelvin} → Fahrenheit {expected}"
            )

    def test_convert_kelvin_to_celsius(self):
        for kelvin, expected in self.test_cases_kelvin_to_celsius:
            self.assertAlmostEqual(
                convertKelvinToCelsius(kelvin),
                expected,
                places=5,
                msg=f"Kelvin {kelvin} → Celsius {expected}"
            )


if __name__ == '__main__':
    unittest.main()
