from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Pessoa(models.Model):
    CHOICES = [
        ("F","Feminino"),
        ("M", "Masculino")
    ]
    nome = models.CharField(null=False, blank=False, max_length=200, verbose_name="Nome da Pessoa")
    sexo = models.CharField(null=True, blank=True,choices=CHOICES, max_length=200, verbose_name="Sexo da Pessoa" )
    data_nascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento")

    class Meta:
        ordering = ["nome", ] 
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
    
    def __str__(self) -> str:
        return f'{self.nome}, {self.get_sexo_display()}'


    