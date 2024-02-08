import requests
from pprint import pprint
API_key="dbe6b548d30ba74ac44ad778fa88124c"
city=input("Enter a City:")
base_url="https://api.openweathermap.org/data/2.5/weather?appid="+API_key+"&q="+city
weather_data=requests.get(base_url).json()
pprint(weather_data)