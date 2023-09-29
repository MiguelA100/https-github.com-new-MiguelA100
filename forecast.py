# Example URL
# https://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&appid=e51ea4695aede89196c9db0c03b5bdf5
import os
import requests
from pprint import pprint
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'https://api.openweathermap.org/data/2.5/forecast'

data = requests.get(url, params=query).json()
pprint(data)

list_of_forecast = data['list']

try:
    for forecast in list_of_forecast:
        temp = forecast['main']['temp']
        weather_description = forecast['weather'][0]
        wind_speed = forecast['dt']
        timestamp = forecast['dt']
        forecast_date = datetime.fromtimestamp(timestamp)
        print(f'At {forecast_date} the temperature will be {temp}F{weather_description}{wind_speed}')
except Exception as e:
    print(e)

for forecast in list_of_forecast:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    windspeed = forecast['dt']

    print(f'At {forecast_date} the temperature will be {temp}F')


def forecast(weather_data):
    try:
        list_of_forecasts  = weather_data['list']
        for forecast in list_of_forecasts:
            temp = forecast['main']['temp']
            timestamp = forecast['dt']
            forecast_date = datetime.fromtimestamp(timestamp)
            weather_description = forecast['weather'][0]['description']
            wind_speed = forecast['weather']['description']
            print(f'At {forecast_date} the weather will be {weather_description} and the temperature will be {temp} F')
        return list_of_forecasts
    except KeyError:
        print('This data is not the format expected')
        return 'Unknown'


