# Generated by Django 4.1.3 on 2022-12-21 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('project_image', models.ImageField(blank=True, default='projects/default_project_image.png', null=True, upload_to='projects/', verbose_name='Изображение проекта')),
                ('link', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['-created'],
            },
        ),
    ]
