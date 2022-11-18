from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(verbose_name='Почта')
    name = models.CharField(max_length=128, verbose_name='Имя')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'подписчик'
        verbose_name_plural = 'подписчики'
