# Generated by Django 4.1.3 on 2022-12-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='surname',
            new_name='second_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Имя пользователя'),
        ),
    ]
