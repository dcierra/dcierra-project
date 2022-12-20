from django.db import models
from users_app.models import Profile
import uuid


class Project(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    project_image = models.ImageField(null=True, blank=True, default='projects/default_project_image.png',
                                      verbose_name='Изображение проекта', upload_to='projects/')
    link_github = models.CharField(max_length=100, null=True, blank=True, verbose_name='Ссылка на гитхаб')
    like_total = models.IntegerField(default=0, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name = 'Проект'
        ordering = ['-like_total', '-created']

    @property
    def image_url(self):
        try:
            url = self.project_image.url
        except:
            url = '/images/projects/default_project_image.png'

        return url

    @property
    def reviewers(self):
        queryset = self.review_set.filter(review_body=None).values_list('user__id', flat=True)

        print(queryset)
        return queryset

    @property
    def user_like(self):
        queryset = self.review_set.exclude(value='').exclude(value='dislike').values_list('user__id', flat=True)
        return queryset

    @property
    def user_send_vote(self):
        queryset = self.review_set.exclude(value='').values_list('user__id', flat=True)
        return queryset

    @property
    def likes_count(self):
        reviews = self.review_set.all()
        likes = reviews.filter(value='like').count()

        self.like_total = likes
        self.save()

    def __str__(self):
        return str(self.title)


class Review(models.Model):
    LIKE_TYPE = (
        ('like', 'Like'),
        ('dislike', 'Dislike')
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    review_body = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    value = models.CharField(max_length=200, choices=LIKE_TYPE, verbose_name='Оценка', null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        verbose_name_plural = 'Оценки'
        verbose_name = 'Оценка'
        ordering = ['-created']
        unique_together = [['user', 'project']]
