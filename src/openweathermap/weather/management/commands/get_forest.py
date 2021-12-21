import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime
from openweathermap.weather.models import Sources, Cities

API_KEY = getattr(settings, "WEATHER_API_KEY")

class Command(BaseCommand):
    help = 'Data testing'


    def handle(self, *args, **kwargs):
        self.forcast()

    def forcast(self):

        city_list = Cities.objects.filter(country='UZ').all()[:15]
        for city in city_list:

            # forcasted weather data API
            v = 'http://api.openweathermap.org/data/2.5/forecast?id={}&&units=metric&appid={}'
            a = v.format(city.server_id, API_KEY)
            # accessing the API json data
            full = requests.get(a).json()

            # looping to get value and put it in the dictionary
            for data in full['list']:
                weather_data = {}

                weather_data['feels_like'] = data['main']['feels_like']
                weather_data['temperature'] = data['main']['temp']
                weather_data['temperature_max'] = data['main']['temp_max']
                weather_data['temperature_min'] = data['main']['temp_min']
                weather_data['description'] = data['weather'][0]['description']
                weather_data['icon'] = data['weather'][0]['icon']

                try:
                    model = Sources.objects.get(city=city, dt = data['dt'])
                except Sources.DoesNotExist:
                    model = Sources(city=city, dt=data['dt'])
                    model.day_obj = datetime.fromtimestamp(int(data['dt'])).strftime('%Y-%m-%d %H:%M:%S')
                    model.weather_type = 1

                model.content = weather_data
                model.save()
