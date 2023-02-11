from django.db import models
import uuid
from django.contrib.auth.models import User
from .validators import validate_file_size, validate_file_extension, validate_filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя пользователя')
    first_name = models.CharField(max_length=200, verbose_name='Имя', null=True, blank=True)
    second_name = models.CharField(max_length=200, verbose_name='Фамилия', null=True, blank=True)
    email = models.EmailField(max_length=200, verbose_name='Эл. почта')
    about_myself = models.TextField(blank=True, null=True, verbose_name='О себе')
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/',
                                      default='profiles/default_profile_image.png',
                                      verbose_name='Изображение профиля', validators=[validate_file_size])
    city = models.CharField(null=True, blank=True, max_length=200, verbose_name='Город')
    link_vk = models.CharField(max_length=100, null=True, blank=True, verbose_name='Ссылка на вк')
    link_github = models.CharField(max_length=100, null=True, blank=True, verbose_name='Ссылка на гитхаб')
    link_telegram = models.CharField(max_length=100, null=True, blank=True, verbose_name='Ссылка на телеграм')
    resume = models.FileField(null=True, blank=True, upload_to='profiles/resumes/', verbose_name='Резюме',
                              validators=[validate_file_size, validate_file_extension, validate_filename])
    quest_location_id = models.UUIDField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
        ordering = ['created']

    @property
    def image_url(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/profiles/default_profile_image.png'

        return url

    @property
    def count_unread_messages(self):
        return self.messages.filter(is_read=False).count()

    def __str__(self):
        return f'{self.username}'


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отправитель')
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages',
                                  verbose_name='Получатель')
    first_name = models.CharField(max_length=200, verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True, verbose_name='Эл. почта')
    subject = models.CharField(max_length=200, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Содержание письма')
    is_read = models.BooleanField(default=False, null=True, verbose_name='Прочитано')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ['is_read', '-created']
