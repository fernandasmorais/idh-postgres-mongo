# Projeto IDH: Integração PostgreSQL e MongoDB: pasta entrega5

Este projeto realiza a leitura de dados de um arquivo `.txt` com informações de IDH e popula duas bases de dados:

- **PostgreSQL** (banco relacional)
- **MongoDB** (banco não relacional)

Os dados são extraídos de um arquivo separado por `;`, processados com Python e armazenados em ambas as bases para fins de análise posterior.

## Estrutura

- `banco_relacional_idh.py`: popula o banco PostgreSQL
- `banco_norelacional_idh.py`: popula o MongoDB
- `federacao.py`: classe com o modelo de dados
- `federacao_dao_postgres.py`: DAO com operações no PostgreSQL
- `idh.txt`: arquivo de entrada com os dados

## Requisitos

- Python 3
- PostgreSQL
- MongoDB
- Bibliotecas:
  - `psycopg2`
  - `pymongo`

## Execução

```bash
python banco_relacional_idh.py
python banco_norelacional_idh.py
