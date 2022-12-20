from django.contrib import admin
from .models import Project, Review


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'owner',
        'title',
        'created',
    ]
    list_display_links = [
        'id',
        'owner',
        'title',
    ]
    search_fields = [
        'owner',
        'title',
    ]


class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'project',
        'created',
        'value'
    ]
    list_display_links = [
        'id',
        'user',
        'project',
        'value'
    ]
    search_fields = [
        'user',
        'project',
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
