from django.db import models

# Create your models here.
class livro(models.Model):
    numero               = models.DecimalField(decimal_places=4.0 ,max_digits=4)
    nome_do_livro        = models.TextField(blank=False, null=False)
    autores              = models.TextField(default='Desconhecido')
    situacao             = models.BooleanField()
    cadastro_em          = models.DateTimeField(auto_now_add=True)
    cadastrador_do_livro = models.TextField(blank=False, null=False)
    editado_em           = models.DateTimeField(auto_now=True)
    editor_do_livro      = models.TextField(blank=False, null=False)
