from django.urls import path
from subtitle_app import views


urlpatterns = [
    path('', views.subtitle_home_page, name='subtitle_home_page'),
]
