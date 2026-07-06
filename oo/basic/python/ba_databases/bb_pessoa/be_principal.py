# importar o DAO: Data Access Object (camada de acesso a dados)
import bf_DAO as dao

# obter a listas de pessoas
pessoas = dao.retornar_pessoas()

# listar as pessoas
for p in pessoas:
    print(p.nome, p.email, p.telefone)