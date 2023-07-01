import requests
import json
from . import keys
from pprint import pprint


def pexel_pic_url(city, state):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": keys.PEXELS_API_KEY}
    params = {"per_page": 1, "query": f"{city} {state}"}
    response = requests.get(
        url,
        headers=headers,
        params=params,
    )
    # print(response)
    dict_content = json.loads(response.content)
    # pull out url photos ['src']['small']
    pictures_url = dict_content["photos"][0]["src"]["large"]
    return pictures_url


def get_weather_data(city, state):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    print(f"{city}, {state}")
    params = {
        "appid": keys.OPEN_WEATHER_API_KEY,
        "q": f"{city},{state},US",
        "limit": 1,
    }
    response = requests.get(url, params=params)
    pprint(response)
    content = json.loads(response.content)
    pprint(response.content)
    lon = content[0]["lon"]
    lat = content[0]["lat"]
    url_weather = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": keys.OPEN_WEATHER_API_KEY,
    }
    weather_response = requests.get(url_weather, params=weather_params)
    # pprint(weather_response)
    weather_content = json.loads(weather_response.content)
    pprint(weather_content)
    temp = weather_content["main"]["temp"]
    description = weather_content["weather"][0]["description"]

    return {"temp": temp, "description": description}


# pexel_pic_url("Miami", "FL")
# get_weather_data("Miami", "FL")
