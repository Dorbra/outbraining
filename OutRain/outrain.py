#!usr/bin/env
import ipinfo
import requests

ACCESS_KEY = '163483cd70b24e'
WEATHER_API_KEY = '6ef3fcb889918e9d7298fdc71f9879b7'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric'

class Ip(object):
    def __init__(self, city, country, lat, lot):
        self.city = city
        self.country = country
        self.lat = lat
        self.lon = lot


def weather(lat, lon, city, country):
        weather_url = WEATHER_URL.format(lat, lon, WEATHER_API_KEY)
        resp = requests.get(weather_url)
        data = resp.json() # parse response to JSON

        tmpr = data['main']['temp']

        print("The Weather in {}, {} is {} degrees Celsius.".format(city, country, int(tmpr)))

def ip_getter():
    handler = ipinfo.getHandler(ACCESS_KEY)
    data = handler.getDetails()
    return Ip(data.city, data.country, data.latitude, data.longitude)


if __name__ == "__main__":
    ip = ip_getter()
    weather(ip.lat, ip.lon, ip.city, ip.country)
    print("Have a great day! (^-^)")
