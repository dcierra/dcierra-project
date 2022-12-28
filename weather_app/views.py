from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WeatherForm
from .utils import update_weather, get_user_city, get_weather_for_guest, get_weather
from dcierra.utils import paginate, search_data
from .models import Weather


def weather_home_page(request):
    try:
        profile = request.user.profile
    except:
        profile = None

    if profile:
        secondary_cities = profile.weather_set.filter(main_city=False)

        for city in secondary_cities:
            update_weather(profile, city.city)

        cities, search_query = search_data(request, 'weather')
        paginator, custom_range, cities = paginate(request, cities, 3)

        if profile.city:
            update_weather(profile, profile.city)
            weather_main_city = Weather.objects.get(owner=profile, city=profile.city, main_city=True)
            context = {
                        'profile': profile, 'cities': cities, 'custom_range': custom_range, 'paginator': paginator,
                        'weather_main_city': weather_main_city
                       }
        else:
            city_guest = get_user_city(request)
            description, temp, feels_like, pressure, humidity, wind = get_weather_for_guest(city_guest)

            context = {
                        'cities': cities, 'custom_range': custom_range, 'paginator': paginator,
                        'city_guest': city_guest, 'description': description,
                        'temp': temp, 'feels_like': feels_like, 'pressure': pressure, 'humidity': humidity, 'wind': wind
                       }
    else:
        city_guest = get_user_city(request)
        error_message = 'Авторизуйтесь в системе, чтобы у вас была возможность добавлять города для отслеживания.'

        description, temp, feels_like, pressure, humidity, wind = get_weather_for_guest(city_guest)

        context = {
                    'error_message': error_message, 'city_guest': city_guest, 'description': description,
                    'temp': temp, 'feels_like': feels_like, 'pressure': pressure, 'humidity': humidity, 'wind': wind
                   }

    return render(request, 'weather_app/weather_home_page.html', context)


@login_required(login_url='login')
def weather_add_city(request):
    form = WeatherForm()

    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if get_weather(request.POST['city']):
            try:
                Weather.objects.get(owner=request.user.profile, city=request.POST['city'])
                return redirect('weather_home_page')
            except:
                if form.is_valid():
                    weather_city = form.save(commit=False)
                    weather_city.owner = request.user.profile
                    weather_city.save()
                    return redirect('weather_home_page')

    context = {'form': form}
    return render(request, 'weather_app/weather_form.html', context)


@login_required(login_url='login')
def weather_delete_city(request, city_id):
    profile = request.user.profile
    city = get_object_or_404(profile.weather_set, id=city_id)

    if request.method == 'POST':
        city.delete()

    return redirect('weather_home_page')
