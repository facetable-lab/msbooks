from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'name', '__str__')
    list_display_links = ('pk', 'email', 'name')
    list_filter = ('email', 'name')
    search_fields = ('email', 'name')
    ordering = ('email',)


admin.site.register(Subscriber, SubscriberAdmin)
