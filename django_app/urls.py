from django.urls import path
from django_app import views


urlpatterns = [
    path('', views.django_projects, name='django_projects'),
]
