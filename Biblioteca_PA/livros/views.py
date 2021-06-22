from django.shortcuts import render

from .models import livro



def livros_view(request):
    estante = livro.objects.get(numero=373)
    livrinho = {
        'number' : estante
    }
    return render(request, 'livros.html', livrinho)

