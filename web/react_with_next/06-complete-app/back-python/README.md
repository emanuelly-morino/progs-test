# Como instalar as bibliotecas necessárias

É preciso pelo menos uma vez instalar as bibliotecas necessárias para executar o backend. 
Use este comando:

```
uv sync
```

# Como executar

Para executar o backend, use este comando:

```
uv run flask --app src/app run
```

# Como testar

Dentro dos arquivos das rotas existem demonstrações sobre como executar as rotas. Porém, seguem alguns testes:

# Teste de operação do backend

```curl localhost:5000```

# Listagem de dados

<a href="https://gitlab.com/hvescovi/progs/-/blob/main/web/react_with_next/06-complete-app/back-python/src/routes/pessoa.py?ref_type=heads#L15">link</a>

OU

```curl localhost:5000/pessoas```

# Login

<a href="https://gitlab.com/hvescovi/progs/-/blob/main/web/react_with_next/06-complete-app/back-python/src/routes/login.py?ref_type=heads#L14">link</a>

OU

```curl http://localhost:5000/login -X POST -H "Content-Type:application/json" -d '{"login":"admin", "senha":"admin123"}'```

# Incluir uma pessoa

<a href="https://gitlab.com/hvescovi/progs/-/blob/main/web/react_with_next/06-complete-app/back-python/src/routes/pessoa.py?ref_type=heads#L61">link</a>

OU

```curl http://localhost:5000/pessoa -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NDU4NDIwNCwianRpIjoiNDE0NWNhOTUtYzA0NS00Mjk2LThjZjctNjUxNzliZTA5ZTMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODQ1ODQyMDQsImNzcmYiOiJhMmMxNTU4Yy1lNjI0LTQ2OTYtOWRlZi0wZGY5YTg4Mjc0MzMiLCJleHAiOjE3ODQ1ODUxMDR9.C2ZOz5K7Dm90QCXsiGC7BslmHn-DGYsVYRUtmmaPWsI" -H "Content-Type:application/json" -d '{"nome":"Tiago Matos", "email":"tima@gmail.com","telefone":"47 9 8899 7766", "login":"tima","senha":"tima123"}'```

Observação: note que a *token* é gerada após o sucesso da execução do login. No exemplo de incluir pessoa, portanto, o valor de token usado no curl deve ser *substituído* pelo valor que for retornado na execução da rota *login*.

