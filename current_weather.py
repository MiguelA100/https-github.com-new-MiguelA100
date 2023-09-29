from pprint import pprint
import requests
import os

key = os.environ.get('WEATHER_KEY')
print(key)


url = f'http://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperials&appid=0c4f9197db3df8e0ee414d799893dd2b'
city = input('Enter the city: ')
country = input('Enter the 2-letter country code: ')
location = f'{city}, {country}'

query = {'q': 'tokyo,jp', 'units': 'celsius', 'appid': key}
data = requests.get(url, params=query).json()

pprint(data)

temp = data['main']['temp']
print(f'The current temperature is {temp} F')
