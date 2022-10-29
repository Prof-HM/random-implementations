# Weather of city
#	Step1: Create account at https://openweathermap.org
#	Step2: Retrieve your personal api https://home.openweathermap.org/api_keys
#	Step3: Install requests package as pre-requiste, through the command prompt

#Install requests with "pip install requests"

#import requests
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "copy & paste your api key here"

def get_weather_details(city):
    try:
        url = BASE_URL + "?q=" + city + "&APPID=" + API_KEY
        response = requests.get(url).json()
        temp_kelvin = response["main"]["temp"]
        temp_cel = int(temp_kelvin - 273.15)
        humidity = response["main"]["humidity"]
        description = response["weather"][0]["description"]
        print(f"\nTemperature of {city} is {temp_cel}°C with {description}")
        print(f"\nExpected Humidity is {humidity}")
    except Exception as e:
        print("Something went wrong")

get_weather_details("Selangor")