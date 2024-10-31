# Syrax
#### API de um sistema de transações bancárias.
___
## Iniciando o projeto
Abaixo terão dois métodos para execução do serviço, via poetry e por meio dos dockerfile. O método recomendado é a utilização do docker.
- Python: Python 3.12
- Docker: Docker version 27.2.0
- Docker Compose version v2.29.2-desktop.2

### Observação:
- O arquivo .env foi adicionado no repositório para facilitar os testes. Não é uma boa prática.
___

## Iniciando o projeto com o docker
Certifique-se de que está no diretório raiz do projeto.

Execute o seguinte comando para subir a api em fast_api e o postgres para o funcionamento:
`docker-compose up -d`

Confira se os serviços estão funcionando com o seguinte comando:
`docker-compose ps`

Você verá algo semelhante:
~~~bash
NAME          IMAGE       COMMAND                  SERVICE   CREATED         STATUS         PORTS
postgres-db   postgres    "docker-entrypoint.s…"   db        1 minutes ago   Up 2 seconds   0.0.0.0:5432->5432/tcp
syrax-api     syrax-api   "poetry run python3 …"   api       1 minutes ago   Up 2 seconds   0.0.0.0:8015->8015/tcp
~~~
___
## Iniciando o projeto com o poetry

### Passo 1
Instale o poetry (https://python-poetry.org/docs/). 

### Passo 2
Após este passo entre na pasta raiz do projeto e execute o comando poetry shell para criar o virtual enviroment do projeto:
`poetry shell`

### Passo 3
Instalar as dependências utilizando o comando poetry install:
`poetry install`

### Passo 4
Suba o serviço do postgres necessário para a persistência dos dados
`docker-compose up -d db`

### Passo 5
Lembre-se de estar no diretório raiz do projeto.
Executar o arquivo main.py para iniciar o projeto com o seguinte comando. 
`python3 main.py`

Você verá algo semelhante:
~~~bash
Server is ready at URL 0.0.0.0:8015/syrax-bank
                               _                 _                     _
 ___ _   _ _ __ __ ___  __    | |__   __ _ _ __ | | __      __ _ _ __ (_)
/ __| | | | '__/ _` \ \/ /____| '_ \ / _` | '_ \| |/ /____ / _` | '_ \| |
\__ \ |_| | | | (_| |>  <_____| |_) | (_| | | | |   <_____| (_| | |_) | |
|___/\__, |_|  \__,_/_/\_\    |_.__/ \__,_|_| |_|_|\_\     \__,_| .__/|_|
     |___/                                                      |_|

INFO:     Started server process [6820]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8015 (Press CTRL+C to quit)
~~~~
___

## Swagger - Documentação
É possível testar as requisições pelo link abaixo após rodar o projeto:
> http://localhost:8015/syrax-bank/docs
___

## Endpoints criados no conceito restfull

### 1 - Create new account.
- Rota HTTP: `| POST | http://localhost:8015/syrax-bank/accounts`
> _Cria uma nova conta "bancaria"no sistema._

#### Parâmetros da requisição:
| Parâmetro | Descrição                  | Obrigatório | Exemplo             |
|-----------|----------------------------|-------------|---------------------|
| balance   | Saldo inicial              | Sim         |10.00                |

O valor pode ser zero.

- Resposta JSON:
```json
{
  "status": true,
  "message": "New account created successfully ",
  "payload": {
    "account_id": "41ef2369-c24a-45c9-adff-0ef603aace88"
  }
}
```
### 2 - List accounts.
- Rota HTTP: `| GET | http://localhost:8015/syrax-bank/accounts`
> _Lista todas as contas do sistema._

- Resposta JSON:
```json
{
  "status": true,
  "payload": [
    {
      "account_id": "3380d891-85e4-4a02-9ae2-8a473f875c0d",
      "balance": "34000.94",
      "created_at": "2024-10-28T17:40:48.077827Z"
    },
    {
      "account_id": "03e77b6d-d912-4134-ac77-faab902114ed",
      "balance": "5994.86",
      "created_at": "2024-10-29T12:11:35.206956Z"
    },
  ]
}
```
### 3 - Checking account deposit.
- Rota HTTP: `| POST | http://localhost:8015/syrax-bank/accounts/{account_id}/deposit`
> _Deposita uma quantia em uma determinada conta._

#### Parâmetros da requisição:
| Parâmetro  | Descrição                  | Obrigatório | Exemplos                             |
|----------- |----------------------------|-------------|------------------------------------- |
| account_id | uuid gerado no cadastro    | Sim         | 3380d891-85e4-4a02-9ae2-8a473f875c0d |
| amount     | quantia a ser depositada   | Sim         | 100.00 | 15.0 | 100                  |

- Resposta JSON:
```json
{
  "status": true,
  "message": "Operation successfully completed: deposit.",
  "payload": {
    "amount": "20.00",
    "account_id": "5df160f5-55d7-45b7-87a8-fb6d207224d7",
    "operation": "deposit"
  }
}
```
### 4 - Checking account withdraw.
- Rota HTTP: `| POST | http://localhost:8015/syrax-bank/accounts/{account_id}/withdraw`
> _Saque de uma quantia em uma determinada conta._

#### Parâmetros da requisição:
| Parâmetro  | Descrição                  | Obrigatório | Exemplos                             |
|----------- |----------------------------|-------------|------------------------------------- |
| account_id | uuid gerado no cadastro    | Sim         | 3380d891-85e4-4a02-9ae2-8a473f875c0d |
| amount     | quantia a ser depositada   | Sim         | 100.00 | 15.0 | 100                  |

- Resposta JSON:
```json
{
  "status": true,
  "message": "Operation successfully completed: withdraw.",
  "payload": {
    "amount": "5.00",
    "account_id": "5df160f5-55d7-45b7-87a8-fb6d207224d7",
    "operation": "withdraw"
  }
}
```
### 5 - Transfer between accounts.
- Rota HTTP: `| POST | http://localhost:8015/syrax-bank/accounts/{account_id}/transfer`
> _Trabsferência de uma quantia entre contas._

#### Parâmetros da requisição:
| Parâmetro         | Descrição                  | Obrigatório | Exemplos                             |
|-------------------|----------------------------|-------------|------------------------------------- |
| account_id        | uuid gerado no cadastro    | Sim         | 4e2970a8-fd92-4e4e-9ebe-ac528eefa006 |
| target_account_id | uuid gerado no cadastro    | Sim         | 5df160f5-55d7-45b7-87a8-fb6d207224d7 |
| amount            | quantia a ser depositada   | Sim         | 100.00 | 15.0 | 100                  |

- Resposta JSON:
```json
{
  "status": true,
  "message": "Operation successfully completed: transfer.",
  "payload": {
    "amount": "50.55",
    "account_id": "4e2970a8-fd92-4e4e-9ebe-ac528eefa006",
    "operation": "transfer",
    "target_account_id": "5df160f5-55d7-45b7-87a8-fb6d207224d7"
  }
}
```

### 5 - List transactions.
- Rota HTTP: `| POST | http://localhost:8015/syrax-bank/accounts/{account_id}/transactions`
> _Lista todas transações bancárias de uma conta._

#### Parâmetros da requisição:
| Parâmetro         | Descrição                  | Obrigatório | Exemplos                             |
|-------------------|----------------------------|-------------|------------------------------------- |
| account_id        | uuid gerado no cadastro    | Sim         | 4e2970a8-fd92-4e4e-9ebe-ac528eefa006 |

- Resposta JSON:
```json
{
  "status": true,
  "payload": {
    "transactions": [
      {
        "amount": "15.00",
        "account_id": "5df160f5-55d7-45b7-87a8-fb6d207224d7",
        "cash_flow": "cash_in",
        "operation": "deposit",
        "transaction_id": 20,
        "transaction_datetime": "2024-10-29T13:36:59.279046Z"
      },
      {
        "amount": "5.00",
        "account_id": "5df160f5-55d7-45b7-87a8-fb6d207224d7",
        "cash_flow": "cash_out",
        "operation": "withdraw",
        "transaction_id": 26,
        "transaction_datetime": "2024-10-29T14:17:56.976014Z"
      },
      {
        "amount": "50.55",
        "account_id": "5df160f5-55d7-45b7-87a8-fb6d207224d7",
        "cash_flow": "cash_in",
        "operation": "transfer",
        "transaction_id": 28,
        "transaction_datetime": "2024-10-29T14:23:15.534205Z"
      }
    ]
  }
}
```

## HttpStatusCode

### OK
- **Código HTTP:** `200 Sucess `
- Lançado para requisições com sucesso

### Created
- **Código HTTP:** `201 Created `
- Lançado para requisições com sucesso na criação de conta


### BadRequest
- **Código HTTP:** `400 Bad Request `
- Erro lançado quando o servidor não consegue processar a requisição por conta de um problema de sintaxe ou semântica dos dados.


### InternalServerError
- **Código HTTP:** `500 Internal Server Error`
- Erro lançado quando uma condição inesperada acontece no servidor.

---

### Rodando script concurrency asyncio que simula as operações da "tabela verdade" do desafio. 
#### Lembre-se de estar no diretório raiz do projeto e com a virtual env ativada. Essa etapa pode ser feita utilizando o pip e uma env padrão, caso prefira.

Com o poetry instalado, ative a virtual env com o comando: `poetry shell`

Agora adcione o httpx: `poetry add httpx`



Rode o script com o seguinte comando: `python3 scripts/concurrency_asyncio.py`

Deverá ver algo parecido com isso no terminal:
~~~bash
{'status': True, 'message': 'Operation successfully completed: deposit.', 'payload': {'amount': '100.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'deposit'}}
84123974-58c1-44b8-a69a-c9086d87e765 0.00
4dd6889d-cf50-43a9-a0bd-bec0582f7483 0.00
46f793c8-78ad-48ce-98ab-1aa09b5cc0d2 100.00
{'status': True, 'message': 'Operation successfully completed: withdraw.', 'payload': {'amount': '50.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'withdraw'}}
84123974-58c1-44b8-a69a-c9086d87e765 0.00
4dd6889d-cf50-43a9-a0bd-bec0582f7483 0.00
46f793c8-78ad-48ce-98ab-1aa09b5cc0d2 50.00
{'status': True, 'message': 'Operation successfully completed: transfer.', 'payload': {'amount': '30.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'transfer', 'target_account_id': '84123974-58c1-44b8-a69a-c9086d87e765'}}
4dd6889d-cf50-43a9-a0bd-bec0582f7483 0.00
46f793c8-78ad-48ce-98ab-1aa09b5cc0d2 20.00
84123974-58c1-44b8-a69a-c9086d87e765 30.00
{'status': True, 'message': 'Operation successfully completed: deposit.', 'payload': {'amount': '50.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'deposit'}}
{'status': True, 'message': 'Operation successfully completed: withdraw.', 'payload': {'amount': '30.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'withdraw'}}
4dd6889d-cf50-43a9-a0bd-bec0582f7483 0.00
84123974-58c1-44b8-a69a-c9086d87e765 30.00
46f793c8-78ad-48ce-98ab-1aa09b5cc0d2 40.00
{'status': True, 'message': 'Operation successfully completed: deposit.', 'payload': {'amount': '100.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'deposit'}}
{'status': True, 'message': 'Operation successfully completed: transfer.', 'payload': {'amount': '50.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'transfer', 'target_account_id': '84123974-58c1-44b8-a69a-c9086d87e765'}}
4dd6889d-cf50-43a9-a0bd-bec0582f7483 0.00
46f793c8-78ad-48ce-98ab-1aa09b5cc0d2 90.00
84123974-58c1-44b8-a69a-c9086d87e765 80.00
{'status': True, 'message': 'Operation successfully completed: transfer.', 'payload': {'amount': '10.00', 'account_id': '84123974-58c1-44b8-a69a-c9086d87e765', 'operation': 'transfer', 'target_account_id': '4dd6889d-cf50-43a9-a0bd-bec0582f7483'}}
{'status': True, 'message': 'Operation successfully completed: transfer.', 'payload': {'amount': '20.00', 'account_id': '46f793c8-78ad-48ce-98ab-1aa09b5cc0d2', 'operation': 'transfer', 'target_account_id': '84123974-58c1-44b8-a69a-c9086d87e765'}}
46f793c8-78ad-48ce-98ab-1aa09b5cc0d2 70.00
4dd6889d-cf50-43a9-a0bd-bec0582f7483 10.00
84123974-58c1-44b8-a69a-c9086d87e765 90.00
~~~~
