# Generated by Django 4.1.3 on 2022-12-09 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('full_name', models.CharField(max_length=200, verbose_name='Полное имя')),
                ('email', models.EmailField(max_length=200, verbose_name='Эл. почта')),
                ('about_myself', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('profile_image', models.ImageField(blank=True, default='profiles/default_profile_image.png', null=True, upload_to='profiles/', verbose_name='Изображение профиля')),
                ('link_vk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на вк')),
                ('link_github', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на гитхаб')),
                ('link_telegram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка на телеграм')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['created'],
            },
        ),
    ]
