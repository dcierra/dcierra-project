from django.db import models
import uuid
from .validators import validate_file_size, validate_file_extension


class Subtitle(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'Английский'),
        ('ru', 'Русский'),
        ('de', 'Немецкий'),
    )

    original_file = models.FileField(upload_to='original_files_subtitle/', verbose_name='Файл', validators=[
        validate_file_size, validate_file_extension
    ])
    translation_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, verbose_name='Выберите язык')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ['-created']
