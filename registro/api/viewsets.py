from rest_framework import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet
from registro.models import Pessoa
from .serializers import PessoaSerializer


class PessoaViewSet(ReadOnlyModelViewSet):
    queryset= Pessoa.objects.all()
    serializer_class= PessoaSerializer