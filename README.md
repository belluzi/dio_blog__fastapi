# DIO Blog FastAPI

API simples de blog desenvolvida com FastAPI. O projeto possui autenticação via JWT e rotas protegidas para criação, listagem, atualização e remoção de posts.

## Tecnologias

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- databases com aiosqlite
- PyJWT
- SQLite

## Estrutura do projeto

```text
dio__blog/
  controllers/      # Rotas da API
  models/           # Tabelas SQLAlchemy
  schemas/          # Modelos de entrada
  services/         # Regras de acesso aos dados
  views/            # Modelos de resposta
  database.py       # Configuracao do banco
  main.py           # Aplicacao FastAPI
  security.py       # Autenticacao JWT
```

## Como executar

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute a aplicacao:

```bash
uvicorn dio__blog.main:app --reload
```

A API ficara disponivel em:

```text
http://127.0.0.1:8000
```

A documentacao interativa do FastAPI pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## Autenticacao

Para acessar as rotas de posts, gere um token JWT pela rota de login:

```http
POST /authentication/login
```

Exemplo de corpo da requisicao:

```json
{
  "user_id": 1
}
```

Resposta esperada:

```json
{
  "access_token": "token_jwt"
}
```

Use o token no header das proximas requisicoes:

```http
Authorization: Bearer token_jwt
```

## Endpoints

### Autenticacao

| Metodo | Rota | Descricao |
| --- | --- | --- |
| POST | `/authentication/login` | Gera um token JWT |

### Posts

Todas as rotas abaixo exigem autenticacao via Bearer token.

| Metodo | Rota | Descricao |
| --- | --- | --- |
| POST | `/posts/` | Cria um post |
| GET | `/posts/` | Lista posts |
| PATCH | `/posts/{post_id}` | Atualiza um post |
| DELETE | `/posts/{post_id}` | Remove um post |

Filtros disponiveis na listagem:

| Parametro | Tipo | Descricao |
| --- | --- | --- |
| `published` | boolean opcional | Filtra posts publicados ou nao publicados |
| `limit` | integer | Limita a quantidade de registros retornados |
| `skip` | integer | Define quantos registros devem ser ignorados |

## Exemplos

Criar um post:

```json
{
  "title": "Meu primeiro post",
  "content": "Conteudo do post",
  "published": true
}
```

Atualizar um post:

```json
{
  "title": "Titulo atualizado",
  "published": false
}
```

## Banco de dados

O projeto usa SQLite com o arquivo `blog.db` na raiz do repositorio. As tabelas sao criadas automaticamente ao iniciar a aplicacao.
