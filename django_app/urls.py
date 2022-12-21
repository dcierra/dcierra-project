from django.urls import path
from django_app import views


urlpatterns = [
    path('', views.django_projects, name='django_projects'),

    # crud projects
    path('create-project/', views.django_project_create, name='django_project_create'),
    path('update-project/<str:project_id>/', views.django_project_update, name='django_project_update'),
    path('delete-project/<str:project_id>/', views.django_project_delete, name='django_project_delete'),
]
