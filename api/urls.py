from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('', views.get_routes),
    # Pyqt-projcects
    path('pyqt-projects/', views.get_pyqt_projects),
    path('pyqt-projects/<str:project_id>/', views.get_pyqt_project),
    path('pyqt-projects/<str:project_id>/vote/', views.pyqt_project_vote),
    # Users token
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Inbox / Messages
    path('inbox/', views.get_inbox),
    path('inbox/message/<str:message_id>/', views.get_message),
    path('inbox/delete-all-messages/', views.delete_all_messages),
    path('inbox/message/<str:message_id>/delete-message/', views.delete_message),
    path('inbox/send-message/', views.send_message),
]