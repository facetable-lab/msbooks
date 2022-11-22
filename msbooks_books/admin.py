from django.contrib import admin

from .models import Book, BookImage, Author, Genre, Language


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year', 'language', 'genre')

    class Meta:
        model = Book


class BookImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BookImage._meta.fields]

    class Meta:
        model = BookImage


class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Author._meta.fields]

    class Meta:
        model = Author


class GenreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Genre._meta.fields]

    class Meta:
        model = Genre


class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Language._meta.fields]

    class Meta:
        model = Language


admin.site.register(Book, BookAdmin)
admin.site.register(BookImage, BookImageAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Language, LanguageAdmin)
