from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created',
    ]
    list_display_links = [
        'id',
        'title',
    ]
    search_fields = [
        'title',
    ]


admin.site.register(Todo, TodoAdmin)
