from rest_framework import serializers
from main.models import Usuario
from main.models import UsuarioRedeSocial

class UsuarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = [
      'id',
      'nome',
      'email',
      'senha',
      'tipo',
    ]

class UsuarioRedeSocialSerializer(serializers.ModelSerializer):
  class Meta:
    model = UsuarioRedeSocial
    fields = [
      'id',
      'nome',
      'email',
      'tipo',
    ]
