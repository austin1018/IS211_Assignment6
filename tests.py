import conversions
import conversions_refactored
import unittest


CelsiusToKelvin_known_values = ((500.00, 773.15),
                                (490.00, 763.15),
                                (440.00, 713.15),
                                (410.00, 683.15),
                                (380.00, 653.15))

def test_CelsiusToKelvin(test):
    for Celsius, Kelvin in CelsiusToKelvin_known_values:
        result = conversions.convertCelsiusToKelvin(Celsius)
        print("Convert Celsius " + str(Celsius) + " to Kelvin")
        test.assertEqual(Kelvin, result)

CelsiusToFahrenheit_known_values = ((500.00, 932.00),
                                (490.00, 914.00),
                                (440.00, 824.00),
                                (410.00, 770.00),
                                (380.00, 716.00))

def test_CelsiusToFahrenheit(test):
    for Celsius, Fahrenheit in CelsiusToFahrenheit_known_values:
        result = conversions.convertCelsiusToFahrenheit(Celsius)
        print("Convert Celsius " + str(Celsius) + " to Fahrenheit")
        test.assertEqual(Fahrenheit, result)

FahrenheitToKelvin_known_values = ((932.00, 773.15),
                                (914.00, 763.15),
                                (896.00, 753.15),
                                (878.00, 743.15),
                                (860.00, 733.15	))

def test_FahrenheitToKelvin(test):
    for Fahrenheit, Kelvin in FahrenheitToKelvin_known_values:
        result = conversions.convertFahrenheitToKelvin(Fahrenheit)
        print("Convert Fahrenheit " + str(Fahrenheit) + " to Kelvin")
        test.assertEqual(Kelvin, result)

FahrenheitToCelsius_known_values = ((932.00, 500.00),
                                (914.00, 490.00),
                                (896.00, 480.00),
                                (878.00, 470.00),
                                (860.00, 460.00))

def test_FahrenheitToCelsius(test):
    for Fahrenheit, Celsius in FahrenheitToCelsius_known_values:
        result = conversions.convertFahrenheitToCelsius(Fahrenheit)
        print("Convert Fahrenheit " + str(Fahrenheit) + " to Celsius")
        test.assertEqual(Celsius, result)

KelvinToCelsius_known_values = ((773.15,500.00),
                                (763.15,490.00),
                                (753.15,480.00),
                                (743.15,470.00),
                                (733.15,460.00))

def test_KelvinToCelsius(test):
    for Kelvin, Celsius in KelvinToCelsius_known_values:
        result = conversions.convertKelvinToCelsius(Kelvin)
        print("Convert Kelvin " + str(Kelvin) + " to Celsius")
        test.assertEqual(Celsius, result)

KelvinToFahrenheit_known_values = ((773.15,932.00),
                                (763.15,914.00),
                                (753.15,896.00),
                                (743.15,878.00),
                                (733.15,860.00))

def test_KelvinToFahrenheit(test):
    for Kelvin, Fahrenheit in KelvinToFahrenheit_known_values:
        result = conversions.convertKelvinToFahrenheit(Kelvin)
        print("Convert Kelvin "+str(Kelvin)+" to Fahrenheit")
        test.assertEqual(Fahrenheit, result)

known_values = (("Celsius","Kelvin",500.00, 773.15),
                ("Celsius","Kelvin",490.00, 763.15),
                ("Celsius","Kelvin",440.00, 713.15),
                ("Celsius","Kelvin",410.00, 683.15),
                ("Celsius","Kelvin",380.00, 653.15),

                ("Celsius","Fahrenheit",500.00, 932.00),
                ("Celsius","Fahrenheit",490.00, 914.00),
                ("Celsius","Fahrenheit",440.00, 824.00),
                ("Celsius","Fahrenheit",410.00, 770.00),
                ("Celsius","Fahrenheit",380.00, 716.00),

                ("Fahrenheit","Kelvin",932.00, 773.15),
                ("Fahrenheit","Kelvin",914.00, 763.15),
                ("Fahrenheit","Kelvin",896.00, 753.15),
                ("Fahrenheit","Kelvin",878.00, 743.15),
                ("Fahrenheit","Kelvin",860.00, 733.15),

                ("Fahrenheit","Celsius",932.00, 500.00),
                ("Fahrenheit","Celsius",914.00, 490.00),
                ("Fahrenheit","Celsius",896.00, 480.00),
                ("Fahrenheit","Celsius",878.00, 470.00),
                ("Fahrenheit","Celsius",860.00, 460.00),

                ("Kelvin","Celsius",773.15,500.00),
                ("Kelvin","Celsius",763.15,490.00),
                ("Kelvin","Celsius",753.15,480.00),
                ("Kelvin","Celsius",743.15,470.00),
                ("Kelvin","Celsius",733.15,460.00),

                ("Kelvin","Fahrenheit",773.15,932.00),
                ("Kelvin","Fahrenheit",763.15,914.00),
                ("Kelvin","Fahrenheit",753.15,896.00),
                ("Kelvin","Fahrenheit",743.15,878.00),
                ("Kelvin","Fahrenheit",733.15,860.00),

                ("Miles","Yards",10.00, 17600.00),
                ("Miles","Yards",100.00, 176000.00),

                ("Miles","Meters",10.00, 16093.40),
                ("Miles","Meters",100.00, 160934.00),

                ("Yards","Miles",17600.00, 10.00),
                ("Yards", "Miles", 176000.00, 100.00),

                ("Yards", "Meters", 109.36, 100.00),
                ("Yards", "Meters", 1093.61, 1000.00),

                ("Meters", "Miles", 16093.40, 10.00),
                ("Meters", "Miles", 160934.00, 100.00),

                ("Meters", "Yards", 100.00, 109.36),
                ("Meters", "Yards", 1000.00, 1093.61),

                )

def test_conversion(test):
    for fromUnit, toUnit, fromValue, toValue in known_values:
        result = conversions_refactored.convert(fromUnit, toUnit, fromValue)
        print("Convert "+fromUnit+" "+str(fromValue)+" to "+toUnit)
        test.assertEqual(toValue, result)

def main():
    test = unittest.TestCase()

    # test_CelsiusToKelvin(test)
    # test_CelsiusToFahrenheit(test)
    # test_FahrenheitToKelvin(test)
    # test_FahrenheitToCelsius(test)
    # test_KelvinToCelsius(test)
    # test_KelvinToFahrenheit(test)

    test_conversion(test)


if __name__ == '__main__':
    main()