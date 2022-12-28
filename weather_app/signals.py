from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Weather
from users_app.models import Profile


@receiver(post_save, sender=Profile)
def profile_update(sender, instance, **kwargs):
    profile = instance
    city = profile.city

    if city:
        try:
            city_already_exist = Weather.objects.get(owner=profile, city=city)
            old_main_city = Weather.objects.get(owner=profile, main_city=True)

            old_main_city.main_city = False
            city_already_exist.main_city = True

            city_already_exist.save()
            old_main_city.save()
        except:
            try:
                old_main_city = Weather.objects.get(owner=profile, main_city=True)
                old_main_city.main_city = False
                old_main_city.save()
            except:
                pass

            weather = Weather.objects.create(owner=profile, city=city, main_city=True)
            weather.save()
