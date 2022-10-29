In this worksheet I will be learning how to get weather details of a city using weather api in python

The data are collected by OpenWeatherMap and can be retrieved by personal api keys provided by the website.
What has been implemented
1. Installing requests package
2. Import requests library
3. Defining the constants (BASE_URL & API_KEY)
4. Creating function to retrieve the data
5. Calling the function

### Variants
Convert kelvin to Celcius and Fahrenheit

    def kelvin_to_celcius_fahrenheit(kelvin):
       celcius = kelvin - 273.15
       fahrenheit = celcius * (9 / 5) + 32
       return int(celcius), int(fahrenheit)
