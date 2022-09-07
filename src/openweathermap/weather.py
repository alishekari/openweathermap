import datetime

import pytz
from django.conf import settings
import requests


class WeatherMiniInfo:
    def __init__(self, min, max, day, description, icon, date):
        self.min = min
        self.max = max
        self.day = day
        self.day = day
        self.description = description
        self.icon_url = f'http://openweathermap.org/img/wn/{icon}@2x.png'
        self.date = date


class Weather:
    openweathermap_api_url = 'https://api.openweathermap.org/data/2.5/onecall?' \
                             'lat={lat}&lon={lon}&appid={token}&units=metric&lang={lang}'

    def __init__(self, lat: float, long: float, lang='en'):
        self.lat = lat
        self.long = long
        self.token = settings.OPENWEATHERMAP_TOKEN
        self.data = None
        self.lang = lang
        self.one_call_api_data()

    def one_call_api_data(self):
        self.data = requests.get(
            url=Weather.openweathermap_api_url.format(lat=self.lat, lon=self.long, token=self.token,
                                                      lang=self.lang)).json()

    def next_seven_days_forecast(self, timezone='Europe/London'):

        daily = self.data['daily']
        forecast = []

        for i in range(8):
            forecast.append(WeatherMiniInfo(min=daily[i]['temp']['min'],
                                            max=daily[i]['temp']['max'],
                                            day=daily[i]['temp']['day'],
                                            description=daily[i]['weather'][0]['description'],
                                            icon=daily[i]['weather'][0]['icon'],
                                            date=datetime.datetime.fromtimestamp(daily[i]['dt'],
                                                                                 tz=pytz.UTC).astimezone(
                                                tz=pytz.timezone(timezone))))
        return forecast
