from django.shortcuts import render
from catalogo.models import Book

# Create your views here.

def indice(request):
    '''
    Página incial de nuestra web
    '''
    libros = Book.objects.all()
    datos = {'autor': 'Luis Miguel', 'libros': libros}
    return render(request, 'index.html', context=datos)