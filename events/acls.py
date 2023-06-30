import requests

from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def pexel_pic_url(city, state):
    url = []
    headers = {"Authorization": PEXELS_API_KEY}
    pictures_url = requests.get(url, headers=headers)
    pictures_url.json()
    return pictures_url


def open_weather(city, state):
    url = []
    headers = {"Authorization": PEXELS_API_KEY}
    weather = requests.get(url, headers=headers)
    weather.json()
    return weather


pexel_pic_url("Miami", "FL")
open_weather("Miami", "FL")
