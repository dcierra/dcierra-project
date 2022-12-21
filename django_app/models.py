from django.db import models
import uuid


class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    project_image = models.ImageField(null=True, blank=True, default='projects/default_project_image.png',
                                      verbose_name='Изображение проекта', upload_to='projects/')
    link = models.CharField(max_length=200, null=True, blank=True, verbose_name='Ссылка')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['-created']

    @property
    def image_url(self):
        try:
            url = self.project_image.url
        except:
            url = '/images/projects/default_project_image.png'

        return url
