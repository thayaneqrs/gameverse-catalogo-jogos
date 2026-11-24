
from django.db import models


class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class Plataforma(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    ano_lancamento = models.PositiveIntegerField()
    classificacao = models.CharField(max_length=20)

    desenvolvedora = models.ForeignKey(
        Desenvolvedora,
        on_delete=models.CASCADE,
        related_name='jogos'
    )

    plataforma = models.ForeignKey(
        Plataforma,
        on_delete=models.CASCADE,
        related_name='jogos'
    )

    def __str__(self):
        return self.nome
