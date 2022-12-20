from django.urls import path
from pyqt_app import views


urlpatterns = [
    path('', views.pyqt_projects, name='pyqt_projects'),
    path('project/<str:project_id>/', views.pyqt_project_page, name='pyqt_project_page'),

    path('projects/<str:project_id>/<str:vote_value>/', views.pyqt_project_vote, name='pyqt_project_vote'),

    # crud projects
    path('create-project/', views.pyqt_project_create, name='pyqt_project_create'),
    path('update-project/<str:project_id>/', views.pyqt_project_update, name='pyqt_project_update'),
    path('delete-project/<str:project_id>/', views.pyqt_project_delete, name='pyqt_project_delete'),
]
