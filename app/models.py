from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    dt_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.id, self.nome)

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    tags = models.ManyToManyField('Categoria')
    dt_cadastro = models.DateTimeField(auto_now_add=True)



