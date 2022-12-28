import requests
from .models import Weather
from django.conf import settings


def get_weather(city):
    weather_api = settings.WEATHER_API
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api}&lang=ru&units=metric'

    weather = requests.get(weather_url).json()
    if weather['cod'] != '404':
        return weather
    else:
        return None



def get_weather_for_guest(city_guest):
    weather_guest = get_weather(city_guest)
    description = weather_guest['weather'][0]['description']
    temp = round(weather_guest['main']['temp'])
    feels_like = round(weather_guest['main']['feels_like'])
    pressure = str(round(weather_guest['main']['pressure'] / 1000 * 750, 2))
    humidity = weather_guest['main']['humidity']
    wind = weather_guest['wind']['speed']

    return description, temp, feels_like, pressure, humidity, wind


def update_weather(profile, city):
    try:
        weather_obj = Weather.objects.get(owner=profile, city=city)
    except:
        weather_obj = Weather.objects.get(owner=profile, city=city, main_city=True)

    weather = get_weather(city)

    description = weather['weather'][0]['description']
    temp = round(weather['main']['temp'])

    if weather_obj.city == profile.city:
        weather_obj.description = description
        weather_obj.temp = temp
        weather_obj.feels_like = round(weather['main']['feels_like'])
        weather_obj.pressure = str(round(weather['main']['pressure'] / 1000 * 750, 2))
        weather_obj.humidity = weather['main']['humidity']
        weather_obj.wind = weather['wind']['speed']
    else:
        weather_obj.description = description
        weather_obj.temp = temp

    weather_obj.save()


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_city(request):
    ip = get_user_ip(request)
    ipgeo_api = settings.IPGEO_API
    api_url = f'https://api.ipgeolocation.io/ipgeo?apiKey={ipgeo_api}&ip={ip}'
    response = requests.get(api_url)
    data = response.json()
    return data['city']
