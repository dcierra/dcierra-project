from django.urls import path
from . import views


urlpatterns = [
    path('character-profile/<str:character_id>/', views.character_profile, name='character_profile'),
    path('create-character/', views.create_character, name='create_character'),
    path('edit-character/<str:character_id>/', views.edit_character, name='edit_character'),
    path('delete-character/<str:character_id>/', views.delete_character, name='delete_character'),

    path('add-location/', views.add_location, name='add_location'),

    path('<str:location_id>/', views.text_quest_home_page, name='text_quest_home_page'),
    path('', views.text_quest_home_page, name='text_quest_home_page'),


    path('edit-location/<str:location_id>/', views.edit_location, name='edit_location'),
    path('delete-location/<str:location_id>/', views.delete_location, name='delete_location'),

    path('add-variant/<str:location_id>/', views.add_variant, name='add_variant'),
    path('edit-variant/<str:variant_id>/<str:location_id>/', views.edit_variant, name='edit_variant'),
    path('delete-variant/<str:variant_id>/<str:location_id>/', views.delete_variant, name='delete_variant'),
]
