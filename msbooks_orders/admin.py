from django.contrib import admin
from .models import Order, Status, BookInOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


class BookInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BookInOrder._meta.fields]

    class Meta:
        model = BookInOrder


admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(BookInOrder, BookInOrderAdmin)
