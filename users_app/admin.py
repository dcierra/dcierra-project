from django.contrib import admin
from .models import Profile, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'first_name',
        'second_name',
        'email',
        'created',
    ]
    list_display_links = [
        'id',
        'user',
    ]
    search_fields = [
        'user',
        'first_name',
        'second_name',
    ]


class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'sender',
        'recipient',
        'subject',
        'created',
    ]
    list_display_links = [
        'id',
        'sender',
        'recipient',
    ]
    search_fields = [
        'sender',
        'recipient',
        'subject',
    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Message, MessageAdmin)
