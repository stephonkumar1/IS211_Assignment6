#Stephon Kumar

class ConversionNotPossible(Exception):
    """Raised when a conversion between incompatible units is attempted."""
    pass

def convert(fromUnit, toUnit, value):
    """Converts a value from one unit to another."""

    # Define conversion factors and formulas
    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    distance_units = ['Miles', 'Yards', 'Meters']

    # Temperature conversions
    if fromUnit == 'Celsius' and toUnit == 'Kelvin':
        return value + 273.15
    elif fromUnit == 'Celsius' and toUnit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif fromUnit == 'Kelvin' and toUnit == 'Celsius':
        return value - 273.15
    elif fromUnit == 'Kelvin' and toUnit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    elif fromUnit == 'Fahrenheit' and toUnit == 'Celsius':
        return (value - 32) * 5/9
    elif fromUnit == 'Fahrenheit' and toUnit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15

    # Distance conversions
    elif fromUnit == 'Miles' and toUnit == 'Yards':
        return value * 1760
    elif fromUnit == 'Miles' and toUnit == 'Meters':
        return value * 1609.34
    elif fromUnit == 'Yards' and toUnit == 'Miles':
        return value / 1760
    elif fromUnit == 'Yards' and toUnit == 'Meters':
        return value * 0.9144
    elif fromUnit == 'Meters' and toUnit == 'Miles':
        return value / 1609.34
    elif fromUnit == 'Meters' and toUnit == 'Yards':
        return value / 0.9144

    # If converting to the same unit, return the value as-is
    elif fromUnit == toUnit:
        return value

    # If the conversion is not possible, raise an exception
    else:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible.")
