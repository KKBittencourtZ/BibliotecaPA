from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.admin import User

# Create your models here.
class livro(models.Model):
    situacao_choices = (
        ('Free', 'Disponível'),
        ('Unfree', 'Emprestado')
    )

    numero               = models.DecimalField(decimal_places=0, max_digits=4, primary_key=True, unique=True, blank=False, null=False)
    nome_do_livro        = models.TextField(blank=False, null=False)
    autores              = models.TextField(default='Desconhecido')
    situacao             = models.CharField(max_length=10, choices=situacao_choices, blank=False, null=False)
    if ObjectDoesNotExist:
        cadastro_em          = models.DateTimeField(auto_now_add=True)
        cadastrador_do_livro = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    else:
        editado_em           = models.DateTimeField(auto_now=True)
        editor_do_livro      = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
