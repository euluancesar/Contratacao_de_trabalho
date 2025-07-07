from django.contrib import admin
from .models import (
    Cidade,
    TipoPessoa,
    Ocupacao,
    AreaContratacao,
    Pessoa,
    Curriculo,
    Vaga,
    Candidatura,
    Empresa
)

admin.site.register(Cidade)
admin.site.register(TipoPessoa)
admin.site.register(Ocupacao)
admin.site.register(AreaContratacao)
admin.site.register(Pessoa)
admin.site.register(Curriculo)
admin.site.register(Vaga)
admin.site.register(Candidatura)
admin.site.register(Empresa)

