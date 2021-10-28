from django.contrib import admin
from registro.models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass
