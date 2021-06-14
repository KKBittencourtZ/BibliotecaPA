from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def login_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def logout_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def cadastro_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def sobre_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def livros_view(request, *args, **kwargs):
    return render(request, 'home.html', {})