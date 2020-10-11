

def convertCelsiusToKelvin(Celsius):
    return 273.15 + Celsius

def convertCelsiusToFahrenheit(Celsius):
    return 1.8*Celsius+32

def convertFahrenheitToKelvin(Fahrenheit):
    return 273.15 + ((Fahrenheit - 32.0) * (5.0/9.0))

def convertFahrenheitToCelsius(Fahrenheit):
    return (Fahrenheit - 32) * 5.0/9.0

def convertKelvinToCelsius(Kelvin):
    return Kelvin - 273.15

def convertKelvinToFahrenheit(Kelvin):
    return 1.8*(Kelvin - 273.15)+32