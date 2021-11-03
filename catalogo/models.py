from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField('Género', max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

class Author(models.Model):
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    date_of_birth = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    date_of_death = models.DateField('Fecha de Fallecimiento', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Book(models.Model):
    '''
    Libro para aplicación de biblioteca ...
    '''
    title = models.CharField('Título', max_length=250)
    summary = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    fecha = models.DateField(blank=True, null=True, help_text='Fecha de publicación')

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, verbose_name='Autor')
    genre = models.ManyToManyField(Genre, verbose_name='Géneros')

    def __str__(self):
        return self.title
    
    def display_genre(self):
        '''Muestra género para admin'''
        return ', '.join([gen.name for gen in self.genre.all()[:3]])
    display_genre.short_description = 'Género'

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'