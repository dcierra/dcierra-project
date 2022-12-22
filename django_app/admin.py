from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
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


admin.site.register(Project, ProjectAdmin)
