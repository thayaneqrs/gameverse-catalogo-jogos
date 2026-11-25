from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Jogo, Desenvolvedora, Plataforma


def listar_jogos(request):
    jogos = Jogo.objects.select_related(
        'desenvolvedora',
        'plataforma'
    ).all()

    # Pesquisa pelo nome ou descrição do jogo
    pesquisa = request.GET.get('pesquisa', '')

    if pesquisa:
        jogos = jogos.filter(
            Q(nome__icontains=pesquisa) |
            Q(descricao__icontains=pesquisa)
        )

    # Filtro por desenvolvedora
    desenvolvedora_id = request.GET.get('desenvolvedora', '')

    if desenvolvedora_id:
        jogos = jogos.filter(desenvolvedora_id=desenvolvedora_id)

    # Filtro por plataforma
    plataforma_id = request.GET.get('plataforma', '')

    if plataforma_id:
        jogos = jogos.filter(plataforma_id=plataforma_id)

    # Ordenação alfabética
    jogos = jogos.order_by('nome')

    # Paginação: 5 jogos por página
    paginator = Paginator(jogos, 5)
    pagina = request.GET.get('page')
    jogos_paginados = paginator.get_page(pagina)

    # Preservar os filtros ao trocar de página
    parametros_paginacao = request.GET.copy()
    parametros_paginacao.pop('page', None)

    contexto = {
        'jogos': jogos_paginados,
        'desenvolvedoras': Desenvolvedora.objects.all(),
        'plataformas': Plataforma.objects.all(),
        'pesquisa': pesquisa,
        'desenvolvedora_selecionada': desenvolvedora_id,
        'plataforma_selecionada': plataforma_id,
        'parametros_paginacao': parametros_paginacao.urlencode(),
    }

    return render(request, 'catalogo/listar_jogos.html', contexto)