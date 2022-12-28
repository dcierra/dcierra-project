from django.db import models
from users_app.models import Profile
import uuid


class Weather(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=200, blank=True, null=True, verbose_name='Город')
    description = models.CharField(max_length=50, blank=True, null=True, verbose_name='Описание')
    temp = models.CharField(max_length=20, blank=True, null=True, verbose_name='Температура')
    feels_like = models.CharField(max_length=20, blank=True, null=True, verbose_name='Ощущается как')
    pressure = models.CharField(max_length=20, blank=True, null=True, verbose_name='Давление')
    humidity = models.CharField(max_length=20, blank=True, null=True, verbose_name='Влажность')
    wind = models.CharField(max_length=20, blank=True, null=True, verbose_name='Скорость ветра')
    main_city = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
