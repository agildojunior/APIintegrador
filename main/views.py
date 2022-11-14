from main.serializers import UsuarioSerializer
from main.serializers import UsuarioRedeSocialSerializer
from rest_framework import viewsets, permissions
from main.models import Usuario
from main.models import UsuarioRedeSocial


class UsuarioViewSet(viewsets.ModelViewSet):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer


class UsuarioRedeSocialViewSet(viewsets.ModelViewSet):
  queryset = UsuarioRedeSocial.objects.all()
  serializer_class = UsuarioRedeSocialSerializer
