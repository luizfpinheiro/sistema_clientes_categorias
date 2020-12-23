from app.models import Categoria, Cliente
from app.serializers import CategoriaSerializer, ClienteSerializer

from rest_framework import viewsets


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer