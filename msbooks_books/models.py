from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'Язык: {self.title} - {self.pk}'

    class Meta:
        verbose_name = 'язык'
        verbose_name_plural = 'языки'


class Book(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True, default=None)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, blank=True, null=True, default=None)
    year = models.CharField(max_length=32, blank=True, null=True, default=None)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, blank=True, null=True, default=None)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Книга: {self.pk} - {self.title} - {self.created}'

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='media/books_images')
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Иоюражение книги: {self.pk} - {self.book} - {self.created}'

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'


class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(blank=True, null=True, default=None)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Писатель: {self.name} - {self.pk}'

    class Meta:
        verbose_name = 'писатель'
        verbose_name_plural = 'писатели'


class Genre(models.Model):
    title = models.CharField(max_length=128, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Жанр: {self.title} - {self.pk}'

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
