# StayFinder

Plataforma demonstrativa de hospedagens por temporada, inspirada em marketplaces de aluguel.

## Funcionalidades do MVP
- Cadastro, login e logout
- Cadastro e edição de anúncios pelo anfitrião
- Busca por destino, capacidade e preço máximo
- Página de detalhes do imóvel
- Solicitação de reservas com cálculo do total
- Validação de datas e prevenção de reservas sobrepostas
- Painel de administração Django
- API REST somente leitura para hospedagens
- Testes automatizados das regras de reserva

## Tecnologias
Python, Django 5.2, Django REST Framework, SQLite, Bootstrap 5 e HTML/CSS.

## Executar no Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
Acesse http://127.0.0.1:8000

## API
- `GET /api/hospedagens/`
- `GET /api/hospedagens/{id}/`

## Testes
```powershell
py manage.py test
```

## Próximas evoluções
- PostgreSQL e variáveis de ambiente
- JWT para autenticação da API
- Favoritos e avaliações
- Upload de múltiplas fotos
- Calendário de disponibilidade
- Pagamento em ambiente sandbox
- Testes de integração e deploy

> Projeto educacional de portfólio. Não é afiliado ao Airbnb e não processa pagamentos reais.
