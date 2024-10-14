#Stephon Kumar

import unittest
import conversions

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        # Test cases for Celsius to Kelvin
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0), 273.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(100), 373.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-273.15), 0)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(300), 573.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(-50), 223.15)

    def test_convertCelsiusToFahrenheit(self):
        # Test cases for Celsius to Fahrenheit
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(0), 32)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(100), 212)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-40), -40)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(300), 572)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-50), -58)

    def test_convertFahrenheitToCelsius(self):
        # Test cases for Fahrenheit to Celsius
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(32), 0)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(212), 100)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(-40), -40)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(572), 300)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(-58), -50)

    def test_convertFahrenheitToKelvin(self):
        # Test cases for Fahrenheit to Kelvin
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(32), 273.15)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(212), 373.15)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(-40), 233.15)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(572), 573.15)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(-58), 223.15)

    def test_convertKelvinToCelsius(self):
        # Test cases for Kelvin to Celsius
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(273.15), 0)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(373.15), 100)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(0), -273.15)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(573.15), 300)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(223.15), -50)

    def test_convertKelvinToFahrenheit(self):
        # Test cases for Kelvin to Fahrenheit
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(273.15), 32)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(373.15), 212)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(0), -459.67, places=2)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(573.15), 572)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(223.15), -58)

if __name__ == '__main__':
    unittest.main()
