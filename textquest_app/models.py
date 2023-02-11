from django.db import models
import uuid


class Location(models.Model):
    location_name = models.CharField(max_length=256, verbose_name='Название локации')
    text = models.TextField(max_length=4096, verbose_name='Текст')
    image = models.ImageField(null=True, blank=True,
                              upload_to='text_quest/',
                              default='text_quest/default_text_quest_image.png',
                              verbose_name='Изображение')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Локации'
        verbose_name = 'Локация'

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = '/images/text_quest/default_text_quest_image.png'

        return url

    def __str__(self):
        return f'{self.location_name}'


class Variant(models.Model):
    title = models.CharField(max_length=256, verbose_name='Вариант')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Локация')
    next_location = models.ForeignKey(Location, related_name='next_location', on_delete=models.CASCADE,
                                      verbose_name='Следующая локация', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'
        ordering = ['created']


class CharacterProfile(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя персонажа')
    version = models.IntegerField(null=True, blank=True, verbose_name='Версия')
    bio = models.TextField(null=True, blank=True, verbose_name='Описание персонажа')
    image = models.ImageField(null=True, blank=True,
                              upload_to='text_quest/characters',
                              default='text_quest/characters/default_character_image.png',
                              verbose_name='Изображение персонажа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'
        ordering = ['created']

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = '/images/text_quest/characters/default_character_image.png'

        return url

