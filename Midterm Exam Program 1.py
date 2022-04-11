class TemperatureConversion:
    def __init__(self, temp):
        self._temp = temp

class CelsiusToFahrenheit(TemperatureConversion):
    def conversion (self):
        cf = (self._temp*9)/5 +32
        return ("%0.2f" % (cf))

class CelsiusToKelvin(TemperatureConversion):
    def conversion(self):
        ck = self._temp + 273.15
        return ("%0.2f" % (ck))

class FahrenheitToCelcius(TemperatureConversion):
    def conversion(self):
        fc = (self._temp - 32.0) * (5.0/9.0)
        return ("%0.2f" % (fc))
class KelvinToCelsius(TemperatureConversion):
    def conversion(self):
        kc = (self._temp - 273.15)
        return ("%0.2f" % (kc))

opt = str(input("What conversion would you like to use?\n1.Celcius to Fahrenheit/Kelvin\n2.Kelvin to Fahrenheit\n3.Fahrenheit to Kelvin\n"))

if opt == "1":
    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

if opt == "2":
    tempinFC = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelcius(tempinFC)
    print(str(convert.conversion()) + " Celsius")

if opt == "3":
    tempinKC = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempinKC)
    print(str(convert.conversion()) + " Celsius")





