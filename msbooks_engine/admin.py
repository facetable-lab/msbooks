from django.contrib import admin

from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', '__str__')
    ordering = ('email',)


admin.site.register(Subscriber, SubscriberAdmin)
