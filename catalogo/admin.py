
from django.contrib import admin
from .models import Jogo, Desenvolvedora, Plataforma


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'ano_lancamento',
        'classificacao',
        'desenvolvedora',
        'plataforma',
    )

    search_fields = ('nome',)

    list_filter = (
        'desenvolvedora',
        'plataforma',
        'ano_lancamento',
    )


@admin.register(Desenvolvedora)
class DesenvolvedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais')
    search_fields = ('nome', 'pais')


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fabricante')
    search_fields = ('nome', 'fabricante')
