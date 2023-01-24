from django.db import models
from users_app.models import Profile
import uuid


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название категории')
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Создатель', null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.title}'


class Todo(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Создатель')
    title = models.CharField(max_length=300, verbose_name='Название задачи')
    description = models.TextField(blank=True, null=True, verbose_name='Описание задачи')
    important = models.BooleanField(default=False, verbose_name='Важная задача')
    date_completed = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория', blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-important', '-created']
