from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def login_view(request, *args, **kwargs):
    return render(request, 'login.html', {})


def logout_view(request, *args, **kwargs):
    return render(request, 'logout.html', {})


def cadastro_view(request, *args, **kwargs):
    return render(request, 'cadastro.html', {})

def sobre_view(request, *args, **kwargs):
    return render(request, 'sobre.html', {})

