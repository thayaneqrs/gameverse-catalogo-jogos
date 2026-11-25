# 🎮 GameVerse — Catálogo de Jogos

## Integrantes
- Lucas
- Thayane

## Sobre o projeto

O GameVerse é um sistema web desenvolvido com Python e Django que permite visualizar e explorar um catálogo de jogos. O projeto foi desenvolvido para a disciplina de Programação para Internet.

O sistema apresenta informações sobre os jogos cadastrados, incluindo nome, descrição, ano de lançamento, classificação indicativa, desenvolvedora e plataforma.

## Funcionalidades

- **Listagem de jogos:** exibe os jogos cadastrados e suas respectivas informações.
- **Pesquisa:** permite pesquisar jogos pelo nome ou pela descrição.
- **Filtro por desenvolvedora:** permite visualizar jogos de uma desenvolvedora específica.
- **Filtro por plataforma:** permite visualizar jogos disponíveis em determinada plataforma.
- **Paginação:** organiza os resultados em páginas de até 5 jogos.
- **Combinação de filtros:** permite utilizar a pesquisa e os filtros simultaneamente.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML5
- CSS3

## Modelos do sistema

O projeto possui três modelos principais:

- **Jogo:** armazena as informações dos jogos.
- **Desenvolvedora:** armazena os dados das empresas responsáveis pelo desenvolvimento dos jogos.
- **Plataforma:** armazena os dados das plataformas dos jogos.

## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/thayaneqrs/gameverse-catalogo-jogos.git
   ```

2. Entre na pasta do projeto:
   ```bash
   cd gameverse-catalogo-jogos
   ```

3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Instale o Django:
   ```bash
   pip install django
   ```

5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Acesse no navegador:
   http://127.0.0.1:8000/

## Demonstração

A captura de tela da aplicação será apresentada nesta seção.

![Tela inicial do GameVerse](imagens/gameverse.png)