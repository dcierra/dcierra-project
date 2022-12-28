from django.urls import path
from . import views


urlpatterns = [
    path('', views.weather_home_page, name='weather_home_page'),

    path('add-city/', views.weather_add_city, name='weather_add_city'),
    path('delete-city/<str:city_id>/', views.weather_delete_city, name='weather_delete_city'),
]
