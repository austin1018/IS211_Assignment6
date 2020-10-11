
def convert(fromUnit,toUnit,value):
    available_convert=[("Celsius","Kelvin")
        , ("Celsius", "Fahrenheit")
        , ("Fahrenheit", "Celsius")
        , ("Fahrenheit", "Kelvin")
        , ("Kelvin", "Celsius")
        , ("Kelvin", "Fahrenheit")
        , ("Miles", "Yards")
        , ("Miles", "Meters")
        , ("Yards", "Miles")
        , ("Yards", "Meters")
        , ("Meters", "Miles")
        , ("Meters", "Yards")
    ]
    if fromUnit==toUnit:
        return value
    if (fromUnit,toUnit) not in available_convert:
        raise Exception("Conversion is not possible")
    elif (fromUnit,toUnit) == ("Celsius","Kelvin"):
        return round(273.15 + value,2)
    elif (fromUnit,toUnit) == ("Celsius", "Fahrenheit"):
        return round(1.8*value+32,2)
    elif (fromUnit,toUnit) == ("Fahrenheit", "Celsius"):
        return round((value - 32) * 5.0/9.0,2)
    elif (fromUnit,toUnit) == ("Fahrenheit", "Kelvin"):
        return round(273.15 + ((value - 32.0) * (5.0/9.0)),2)
    elif (fromUnit,toUnit) == ("Kelvin", "Celsius"):
        return round(value - 273.15,2)
    elif (fromUnit,toUnit) == ("Kelvin", "Fahrenheit"):
        return round(1.8*(value - 273.15)+32,2)

    elif (fromUnit,toUnit) == ("Miles", "Yards"):
        return round(1760.0 * value,2)
    elif (fromUnit,toUnit) == ("Miles", "Meters"):
        return round(1609.34 * value,2)
    elif (fromUnit,toUnit) == ("Yards", "Miles"):
        return round(value / 1760.0,2)
    elif (fromUnit,toUnit) == ("Yards", "Meters"):
        return round(value / 1.09361,2)
    elif (fromUnit,toUnit) == ("Meters", "Miles"):
        return round(0.000621371 * value,2)
    elif (fromUnit,toUnit) == ("Meters", "Yards"):
        return round(1.09361 * value,2)