# pony com sqlite e mysql

## Execução

Para rodar os programas, utilize:

```uv run exemplo01_sqlite.py```

e

```uv run --env-file .env exemplo02.py```

# Variáveis de ambiente (exemplo02)

Deve haver um arquivo .env com estas variáveis (modifique os valores conforme sua necessidade de conexão a banco de dados):

```
DATABASE_NAME=ifcblu2026
DATABASE_HOST=localhost
DATABASE_USER=root
DATABASE_PASSWORD=root
DATABASE_PORT=3306
```

Lembre-se de:
a) alterar os valores das variáveis de ambiente dentro do arquivo .env
b) adicionar ao .gitignore o arquivo .env
