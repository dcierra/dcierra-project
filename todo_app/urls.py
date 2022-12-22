from django.urls import path
from todo_app import views


urlpatterns = [
    path('', views.home_page, name='todo_home_page'),

    # crud todos
    path('create/', views.todo_create, name='todo_create'),
    path('update/<str:todo_id>/', views.todo_update, name='todo_update'),
    path('delete/<str:todo_id>/', views.todo_delete, name='todo_delete'),
    path('complete/<str:todo_id>/', views.todo_complete, name='todo_complete'),
    path('uncompleted/<str:todo_id>/', views.todo_uncompleted, name='todo_uncompleted'),
]
