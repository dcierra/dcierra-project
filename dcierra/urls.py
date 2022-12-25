from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static, serve

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('users_app.urls')),
    path('pyqt-projects/', include('pyqt_app.urls')),
    path('django-projects/', include('django_app.urls')),
    path('api/', include('api.urls')),

    # django projects
    path('todo/', include('todo_app.urls')),
    path('subtitle-translate/', include('subtitle_app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            serve, {'document_root': settings.STATIC_ROOT}),
    ]
