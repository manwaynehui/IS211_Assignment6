# conversions.py

def convertCelsiusToKelvin(celsius: float) -> float:
    """Celsius → Kelvin"""
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius: float) -> float:
    """Celsius → Fahrenheit"""
    return celsius * 9.0 / 5.0 + 32.0


def convertFahrenheitToCelsius(fahrenheit: float) -> float:
    """Fahrenheit → Celsius (spelling corrected)"""
    return (fahrenheit - 32.0) * 5.0 / 9.0


def convertFahrenheitToKelvin(fahrenheit: float) -> float:
    """Fahrenheit → Kelvin"""
    return (fahrenheit + 459.67) * 5.0 / 9.0


def convertKelvinToCelsius(kelvin: float) -> float:
    """Kelvin → Celsius"""
    return kelvin - 273.15


def convertKelvinToFahrenheit(kelvin: float) -> float:
    """Kelvin → Fahrenheit"""
    return kelvin * 9.0 / 5.0 - 459.67

