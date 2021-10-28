from django.db.models import fields
from rest_framework import serializers

from ..models import Pessoa 


class PessoaSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()
    sexo = serializers.CharField()
    data_nascimento = serializers.DateField()

    class Meta:
        model= Pessoa 
        fields= [
            "nome",
            "sexo",
            "data_nascimento",
        ]

