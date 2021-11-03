from django.contrib import admin

# Register your models here.
from .models import Book, Author, Genre

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    list_filter = ('author', 'genre')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    fieldsets = (('Datos personales', {'fields' : [('first_name', 'last_name')]}), ('Fechas', {'fields': [('date_of_birth', 'date_of_death')]}))

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass