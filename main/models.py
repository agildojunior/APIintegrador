from django.db import models

# Create your models here.

usuarios_tipos = (
    (1, "Usuario"),
    (2, "Admin"),
  )

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=100)
    tipo = models.IntegerField(choices=usuarios_tipos, default=1)

    def __str__(self):
        return self.nome


class UsuarioRedeSocial(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tipo = models.IntegerField(choices=usuarios_tipos, default=1)

    def __str__(self):
        return self.nome