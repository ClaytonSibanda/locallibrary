from django.contrib import admin
from catalog.models import Book, BookInstance, Author,Language, Genre
# Register your models here.

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
