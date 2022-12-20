from django.urls import path
from users_app import views


urlpatterns = [
    path('', views.home_page, name='home_page'),

    # Login/Register/Logout
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Account/Profile Page
    path('account/', views.account_page, name='account'),
    path('account-edit', views.account_edit, name='account_edit'),
    path('profile/<str:profile_id>/', views.profile_user, name='profile_user'),
    path('profiles/', views.profiles, name='profiles'),

    # Messages/Inbox
    path('inbox/', views.inbox, name='inbox'),
    path('send-message/<str:profile_id>/', views.send_message, name='send_message'),
    path('message/<str:message_id>/', views.message_page, name='message_page'),

    path('message-delete/<str:message_id>/', views.message_delete, name='message_delete'),
    path('all-messages-delete/', views.all_messages_delete, name='all_messages_delete'),
]
