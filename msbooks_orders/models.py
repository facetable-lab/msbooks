from django.db import models

from msbooks_books.models import Book


class Status(models.Model):
    title = models.CharField(max_length=32)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Статус: {self.title}'

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Order(models.Model):
    user_name = models.CharField(max_length=32)
    user_email = models.EmailField(blank=True, null=True, default=True)
    user_phone = models.CharField(max_length=32, blank=True, null=True, default=True)

    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    comments = models.CharField(max_length=256)

    def __str__(self):
        return f'Заказ: {self.status} - {self.pk} - {self.user_email}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class BookInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    book = models.ForeignKey(Book, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Книги в заказе: {self.pk} - {self.product} - {self.created}'

    class Meta:
        verbose_name = 'книга в заказе'
        verbose_name_plural = 'книги в заказе'
